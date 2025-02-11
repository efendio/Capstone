from django.urls import path
from . import views
app_name = 'Formosa'

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),
    path('blank/', views.blank, name='blank'),

]
