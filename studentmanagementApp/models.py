from django.db import models



# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

# class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField ()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def age_condition(self):
        if self.age <= 22:
            return "Eligible"
        else:
            return "Not Eligible"
        
    def email_confiton(self):
        if self.email.endswith('@gmail.com'):
            return "Valid"
        else:
            return "Invalid"


    def __str__(self):
        return self.name