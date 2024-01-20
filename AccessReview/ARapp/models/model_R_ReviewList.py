from django.db import models
import django_tables2 as tables
from django import forms
import datetime

from .model_Countries import Country
from .model_Systems import Systems



class R_ReviewList(models.Model):
    name = models.CharField(max_length=255)
#    system = models.CharField(max_length=255)  ##TODO change to system_ID and reference systemID from model_Systems.py
    system = models.ForeignKey(Systems, on_delete=models.PROTECT)       ##TODO think about cascade not protect  - https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    country = models.ForeignKey(Country, on_delete=models.PROTECT)      ##TODO think about cascade not protect
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

    
    def __str__(self):
        """Returns a string representation of a review list."""
        return self.name
    

class ReviewListTable(tables.Table):
    class Meta:
        model = R_ReviewList
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "system", "country", )
    ##TODO modify to pull data based on selected system
    # Select = tables.TemplateColumn('''
    #                                 <a href="/systems/{{ record.id }}">Select</a> 
    #                                 <a href="/schedule/delete_schedule/{{ record.id }}" 
    #                                     onclick="return confirm('Are you sure you want to delete this?')">on click test</a>''')

class ReviewListForm(forms.ModelForm):
    class Meta:
        model = R_ReviewList
        # fields = "__all__"
        fields = ("name", "system", "country")