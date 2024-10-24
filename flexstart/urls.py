"""flexstart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flexstart import settings
from registration import urls
from core import urls
from services import urls
from portfolio import urls
from testimonials import urls
from blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("registration.urls")),
    # CORE URLs
    path("", include("core.urls")),
    # SERVICES URLs
    path("", include("services.urls")),
    # PORTFOLIO URLs
    path("", include("portfolio.urls")),
    # TESTIMONIALS URLs
    path("", include("testimonials.urls")),
    # BLOG URLs
    path("", include("blog.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)