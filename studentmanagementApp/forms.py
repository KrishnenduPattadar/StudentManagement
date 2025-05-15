from django import forms
from .models import Student  # Ensure the correct model is imported
from django.core.exceptions import ValidationError
 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  # Specify the model class
        fields = ['student_id', 'name', 'age', 'department', 'email', 'city', 'fees', 'gender', 'image',]  # Include all relevant fields        
    
    
    def clean_student_id(self): #we write this condition on form.py becuase we want to validate the data before saving it to the database
        student_id = self.cleaned_data.get('student_id')

        if not student_id.startswith('CIPL'):
            raise forms.ValidationError("Your student ID must start with 'CIPL'.")
        if len(student_id) != 8:
            raise forms.ValidationError("Your student ID must be 8 characters long.")
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError("This student ID already exists.")
        return student_id
    
    def clean_email(self): #we write this condition on form.py becuase we want to validate the data before saving it to the database
        email = self.cleaned_data.get('email')

        if not email.endswith('@gmail.com'):
            raise ValidationError("your email must end with '@gmail.com'")
        return email
 


            