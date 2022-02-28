from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registered/', views.registered, name='registered'),
    path('attendance/', views.attendance, name='attendance'),
    path('add/', views.add, name='add'),
    path('delete_items/<str:pk>/', views.delete_items, name='delete_items'),
    path('register/', views.register, name='register'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logout/', views.logout, name='logout'),
    path('calculator/', views.calculator, name='calculator'),
    path('calculator/result', views.result, name='result'),
    
]
