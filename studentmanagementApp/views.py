from django.shortcuts import render, redirect, get_object_or_404
from studentmanagementApp.forms import StudentForm
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

def home(request):
    return render(request, 'studentmanagementApp/home.html')

def resgister_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'studentmanagementApp/index.html', {'form': form})
def success(request):
    return render(request, 'studentmanagementApp/success.html')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentmanagementApp/student_list.html', {'students': students})

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentmanagementApp/edit_student.html', {'form': form})
 
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'studentmanagementApp/confirm_delete.html', {'student': student})

class CustomLoginView(LoginView):
    template_name = 'studentmanagementApp/home.html'

def custom_login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    # print('data', form.is_valid())
    if request.method == 'POST' and form.is_valid():
        from django.contrib.auth import login
        login(request, form.get_user())
        return redirect('register_student')  # Replace with your desired redirect
    return render(request, 'studentmanagementApp/home.html', {'form': form})

# Create your views here.
