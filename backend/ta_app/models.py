from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_ta = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add a custom related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add a custom related_name to avoid conflict
        blank=True
    )

class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.ta.user.username + " - " + self.student.username