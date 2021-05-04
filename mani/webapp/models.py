from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.IntegerField(max_length=2)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname
