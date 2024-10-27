from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q, Count, Prefetch
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post, Comment, Tag
from registration.models import Profile
from .forms  import CommentForm

class Blog(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog.html"
    paginate_by = 3 

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comment')).select_related('author').prefetch_related('tags').order_by('-comment_count')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context

class BlogSearch(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog_search_results.html"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).select_related('author').prefetch_related('tags').distinct()
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["search_query"] = self.request.GET.get('q', '')
        return context

class BlogDetails(DetailView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog-details.html"

    def get_object(self):
        return Post.objects.select_related('author').prefetch_related(
            Prefetch('comment_set', queryset=Comment.objects.filter(parent__isnull=True).select_related('user_published')),
            'tags'
        ).get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context["tags"] = Tag.objects.all()
        context['comments'] = self.object.get_comments()
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            
    
            profile = get_object_or_404(Profile, user=request.user)
            comment.user_published = profile 
            
    
            parent_id = request.POST.get('parent')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass  
            
            comment.save()
            return redirect('blog-details', pk=post.pk)

    
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/form/comment_delete.html"
    context_object_name = "object"
    
    def test_func(self):
        comment = self.get_object()

        is_author = self.request.user == comment.user_published.user 
        is_superuser = self.request.user.is_superuser
        is_admin = self.request.user.is_staff 

        return is_author or is_superuser or is_admin
    
    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('blog-details', kwargs={'pk': comment.post.id})
    
