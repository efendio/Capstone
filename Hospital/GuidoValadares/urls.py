from django.urls import path
from . import views
app_name = 'GuidoValadares'

urlpatterns = [
    path('', views.index, name='index'),  
   # path('index2/', views.index2, name='index2'),
    path('about/', views.about, name='about'),
    path('details/', views.details, name='details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors, name='doctors'),
]