from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', post, name='post'),
    path('about/', about, name='about'),
    path('contac/', contac, name='contact'),

]
