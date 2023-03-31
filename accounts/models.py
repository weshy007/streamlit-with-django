from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=50, null=True, blank=True)
    field_of_study = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "User"
