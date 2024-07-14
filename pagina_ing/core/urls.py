# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Esta línea define la URL para la raíz del sitio
    path('login/', views.login, name='login'),
    path('subida_casos/', views.subir_casos, name='subida_casos'),
    path('about/', views.about, name='about'),
    path('advisor/', views.advisor, name='advisor'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('review/', views.review, name='review'),
    path('service/', views.service, name='service'),
    path('single/', views.single, name='single'),
]
