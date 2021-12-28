from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=20,default='')
    Age=models.IntegerField(default='')
    Place=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True,default='')
    Email=models.EmailField(default='')
    Password=models.CharField(max_length=8,default='')
class Photo(models.Model):
    image=models.ImageField(upload_to='media/',null=True,blank=True,default='')
    description=models.TextField()
    def __str__(self):
        return self.description
        