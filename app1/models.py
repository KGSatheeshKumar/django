from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    age = models.IntegerField()
    tenth_per = models.IntegerField()
    twelve_per = models.IntegerField()
    interest_dept = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    
