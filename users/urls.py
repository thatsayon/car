from django.urls import path 
from . import views 

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='Login'),
    path('register/', views.register, name='Register'),
    path('profile/', views.profile, name='Profile'),
    path('logout/', views.user_logout, name='Logout'),
]
