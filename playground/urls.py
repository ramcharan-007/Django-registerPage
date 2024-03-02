from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('dashboard/', views.dashboard, name="dashboard")
]

