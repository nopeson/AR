from django.db import models
import datetime
import django_tables2 as tables

from .model_UserStatusType import UserStatus, UserType


# Create your models here.
class Users(models.Model):
    employee_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    userStatus = models.ForeignKey('UserStatus', on_delete=models.PROTECT, null=True)  #info from bambooHR leave/terminated/live      ##TODO remove null 
    userType = models.ForeignKey('UserType', on_delete=models.PROTECT, null=True)      #info if contractor/employee/system          ##TODO remove null 
#    middleName = models.CharField(max_length=255, blank=True)
#    surName = models.CharField(max_length=255)
#    mail = models.CharField(max_length=255)
#    jobTitle = models.CharField(max_length=255, blank=True)
#    officeLocation = models.CharField(max_length=255, blank=True)
#    managerEmployeeID = models.ForeignKey('self', on_delete=models.CASCADE)
#    isEnabled = models.BooleanField()
#    isAssetOwner = models.BooleanField()
#    lastLoginAD = models.DateTimeField(blank=True, default=datetime.datetime.now())
#    lastLoginAPP = models.DateTimeField(blank=True, default=datetime.datetime.now())

    def __str__(self):
        """Returns a string representation of a message."""
        return self.employee_ID
    

class UsersTable(tables.Table):
    class Meta:
        model = Users
        template_name = "django_tables2/bootstrap.html"
        fields = ("employee_ID", "name", "userStatus.status", "userType.userType", )
