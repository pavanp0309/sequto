"""
URL configuration for SeqtoSoftware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Talento import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# registering the function based urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('UserHome/',views.UserHome,name='UserHome'),
    path('contact/',views.ContactUs,name='Contact'),
    path('register/',views.register,name='register'),
    path('signin/', views.signin, name='signin'),
    path('postjob/', views.Post_Job, name='Post_Job'),
    path('success/', views.success, name='success'),
    path('logout/', views.logout_view, name='logout')
]+static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)