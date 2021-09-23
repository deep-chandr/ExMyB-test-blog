from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('list/', views.BlogsList.as_view(), name='list'),

    path('list/<int:blog_id>/', views.BlogsDetail.as_view(), name='blog_item'),


    path('/', views.index, name='index'),
]
