from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student_name=models.CharField(max_length=255)
    place=models.TextField()
    age=models.IntegerField()
    marks=models.IntegerField()
    user_image=models.ImageField(upload_to='image/')
