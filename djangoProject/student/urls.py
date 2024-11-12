from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name='student_list'),
    path("new/", views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),]