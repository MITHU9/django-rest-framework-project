from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name
