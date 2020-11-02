from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    gender=models.CharField(choices=(('Male','Male'),('Female','Female')),max_length=10)

    def __str__(self):
        return self.name
    