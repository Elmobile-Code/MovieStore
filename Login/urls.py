from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='Login.login'),
    path('signup/', views.signup, name='Login.signup'),
    path('logout/', views.logout, name='Login.logout'),
]
