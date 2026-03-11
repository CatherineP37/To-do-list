from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<task_id>/', views.edit, name="edit"),
    path('not_done/<task_id>/', views.not_done, name="not_done"),
    path('delete/<task_id>/', views.delete, name="delete"),
]