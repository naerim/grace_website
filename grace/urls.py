"""grace_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('introduce/', views.introduce, name='introduce'),
    path('apply/', views.apply, name='apply'),
    path('category/', views.PostList.as_view()),
    path('logout/', views.logout, name='logout'),
    path('myPage/', views.myPage, name='myPage'),
    path('tutor/', views.tutor, name='tutor'),
]
