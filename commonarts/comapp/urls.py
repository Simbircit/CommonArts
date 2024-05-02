from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.exit, name='logout'),
    path('register/', views.register, name='register'),
    path('post/', views.send, name='post'),
    path('', views.mainindex, name="main"),
    path('gallery/', views.gallery, name='gallery')
]
