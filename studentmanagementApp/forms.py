from django import forms
from .models import Student  # Ensure the correct model is imported

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Specify the model class
        fields = ['name', 'age', 'department', 'email', 'city', 'gender', 'image']  # Include all relevant fields