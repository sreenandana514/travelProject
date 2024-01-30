from django.urls import path
from credential import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('Home', views.logout, name='Home'),
    path('About us', views.logout, name='About us')
]
