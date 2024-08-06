from django.contrib import admin
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addArticle/', views.addArticle, name="addArticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('', views.articles, name="articles"),
    path('add_comment/<int:id>', views.add_comment, name="add_comment"),
]