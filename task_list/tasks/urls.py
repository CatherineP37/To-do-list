from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<task_id>/', views.edit, name="edit"),
]