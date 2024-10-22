from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post, Comment, Tag
from registration.models import Profile
from .forms  import CommentForm


# Create your views here.

class Blog(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()

        for post in context['posts']:
            post.comment_count = post.comment_set.count()
        return context

class BlogDetails(DetailView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/blog-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context["tags"] = Tag.objects.all()
        context['comment_count'] = self.object.comment_set.count()
        context['comments'] = self.object.comment_set.filter(parent__isnull=True)  # Solo los comentarios principales
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            
            # Asignar el perfil del usuario autenticado
            profile = get_object_or_404(Profile, user=request.user)
            comment.user_published = profile 
            
            # Obtener el comentario padre (si es una respuesta)
            parent_id = request.POST.get('parent')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass  # Si el comentario padre no existe, se ignora
            
            comment.save()
            return redirect('blog-details', pk=post.pk)

        # Si el formulario no es válido, renderizar la página con errores
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
