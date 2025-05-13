from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    student_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # def clean(self):
    #     super().clean()  # Call the parent class's clean method
    #     if self.student_id and not self.student_id.startswith('CIPL'):
    #         raise ValidationError({'student_id': "Your student ID must start with 'CIPL'."})

    def age_condition(self):
        if self.age <= 22:
            return "Eligible"
        else:
            return "Not Eligible"

    def email_condition(self):
        if self.email.endswith('@gmail.com'):
            return "Valid"
        else:
            return "Invalid"

    def __str__(self):
        return self.name