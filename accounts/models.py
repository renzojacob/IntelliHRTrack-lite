from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)

    def __str__(self):
        return self.username
