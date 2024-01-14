from django.db import models
import datetime

class UserStatus(models.Model):
    status = models.CharField(max_length=255)
    userType = models.CharField(max_length=255)