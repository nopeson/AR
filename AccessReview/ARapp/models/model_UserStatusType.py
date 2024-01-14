from django.db import models
import datetime

class UserStatus(models.Model):
    status = models.CharField(max_length=255)

class UserType(models.Model):
    userType = models.CharField(max_length=255)