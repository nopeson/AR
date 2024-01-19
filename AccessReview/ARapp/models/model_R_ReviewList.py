from django.db import models
import datetime
#from .model_Countries import Country

class R_ReviewList(models.Model):
    name = models.CharField(max_length=255)
    system = models.CharField(max_length=255)  ##TODO change to system_ID and reference systemID from model_Systems.py
    reviewRanBy = models.CharField(max_length=255, null=True) ##TODO change to employee_ID reference
    reviewStart = models.DateTimeField(null=True)
    reviewEnd = models.DateTimeField(null=True)     #this is when the review should end, do not confuse with reviewDone -> thats timestamp when  it actually finished
    allUsersDone = models.BooleanField(default=False)
    allUsersDoneTime = models.DateTimeField(null=True)  ##TODO decide to use DateField.auto_now or DateField.auto_now_add
    allManagersDone = models.BooleanField(default=False)
    allManagersDoneTime = models.DateTimeField(null=True)  ##TODO decide to use DateField.auto_now or DateField.auto_now_add
    assetOwnerDone = models.BooleanField(default=False)
    assetOwnerDoneTime = models.DateTimeField(null=True)  ##TODO decide to use DateField.auto_now or DateField.auto_now_add
    additionalActionsDone = models.CharField(max_length=255, null=True) ##TODO JIRA ticket for SD -> either link a table or just text
    additionalActionsDoneTime = models.DateTimeField(null=True)  ##TODO decide to use DateField.auto_now or DateField.auto_now_add
    reviewDone = models.BooleanField(default=False)
    reviewDoneTime = models.DateTimeField(null=True)  ##TODO decide to use DateField.auto_now or DateField.auto_now_add

    


