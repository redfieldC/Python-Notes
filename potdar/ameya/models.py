from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(default=0,max_length=3)

    def __str__(self):
        return self.first_name