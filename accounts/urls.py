from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('index/', include('mainapp.urls')),
    path('user/<str:username>/', views.user_Profile, name='user_Profile'),
    path('delete_post/<str:pk>/', views.post_delete, name='post_delete'),
    path('edit/<str:username>/', views.edit_user, name='edit_user'),

]
