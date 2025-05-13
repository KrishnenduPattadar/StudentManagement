from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # Set home (login) as the first page
    path('custom_login_view/', views.custom_login_view, name='custom_login_view'),  # Custom login view
    path('register/', views.resgister_student, name='register_student'),  # Registration page
    path('success/', views.success, name='success'),  # Success page
    path('student/', views.student_list, name='student_list'),  # Student list
    path('student/edit/<int:pk>/', views.edit_student, name='edit_student'),  # Edit student
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),  # Delete student
]

