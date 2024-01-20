from django.db import models
import django_tables2 as tables
import datetime

from .model_Countries import Country

class Systems(models.Model):
    systemName = models.CharField(max_length=255)
    criticality = models.CharField(max_length=255)
    systemDescription = models.TextField(null=True)
    #country = models.CharField(max_length=255)
    country = models.ManyToManyField(Country)


    
    def __str__(self):
        """Returns a string representation of a system."""
        return self.systemName
    

class SystemsTable(tables.Table):
    class Meta:
        model = Systems
        template_name = "django_tables2/bootstrap.html"
        fields = ("systemName", "criticality", "country.countryName", )
    ##TODO modify to pull data based on selected system
    Select = tables.TemplateColumn('''
                                    <a href="/systems/{{ record.id }}">Select</a> 
                                    <a href="/schedule/delete_schedule/{{ record.id }}" 
                                        onclick="return confirm('Are you sure you want to delete this?')">on click test</a>''')




#Table Systems{
#  id integer [primary key]
#  systemName varchar
#  criticality varchar
#  accessMatrix_ID integer [ref: - AccessMatrixList.id]
#  country_ID integer [ref: > Countries.id]
#  lastReviewedOn timestamp
#  assetOwner_ID integer [ref: - Users.employee_ID]
#}