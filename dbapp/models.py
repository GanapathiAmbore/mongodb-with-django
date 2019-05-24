from django.db import models
class Student(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.Name

