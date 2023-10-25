from django.db import models

# Create your models here.

class RegistrationModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()
    education=models.CharField(max_length=20,null=True)
    place=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    