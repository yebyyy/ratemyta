from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_ta = models.BooleanField(default=False)

class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One to One field is used to create a one-to-one relationship between two models
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username # Return the username of the user
    
class Review(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.ta.user.username + " - " + self.student.username