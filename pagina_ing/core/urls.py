# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import registro 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),  # Esta línea define la URL para la raíz del sitio
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('registro/', registro, name="registro"),
    path('subida_casos/', views.subir_casos, name='subida_casos'),
    path('about/', views.about, name='about'),
    path('advisor/', views.advisor, name='advisor'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('review/', views.review, name='review'),
    path('service/', views.service, name='service'),
    path('single/', views.single, name='single'),
    path('comment/add/', views.add_comment, name='add_comment'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comment/edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),


]
