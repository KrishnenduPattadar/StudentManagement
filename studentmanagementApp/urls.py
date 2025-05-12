from django.urls import path
from . import views

urlpatterns = [
    path('', views.resgister_student, name='register_student'),
    path('success/', views.success, name='success'),
    path('student/', views.student_list, name='student_list'),
    path('student/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),

]

