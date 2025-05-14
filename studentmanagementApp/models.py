from django.db import models

class Student(models.Model):
    # student_id = models.CharField(max_length=100, null=True, blank=True)
    # name = models.CharField(max_length=100)
    # age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
    ]

# class Student(models.Model):
    student_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField ()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def age_condition(self):
        if self.age <= 22:
            return "You Are Eligible"
        else:
            return "As per your age you are not eligible"
        
    def email_condition(self):
        if self.email.endswith('@gmail.com','@yahoo.com'):
            return "Valid"
        else:
            return "Invalid"
        
    def fees_condition(self):
        if self.fees >= 10000:
            return "Valid"
        else:
            return "Invalid"
        
    # def id_condition(self):
    #     if self.student_id.startswith('S'):
    #         return "Valid"


    def __str__(self):
        return self.name