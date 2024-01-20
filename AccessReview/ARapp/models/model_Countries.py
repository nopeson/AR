from django.db import models
import django_tables2 as tables
import datetime




class Country(models.Model):
    countryName = models.CharField(max_length=255)
    isLive = models.BooleanField()
    
    def __str__(self):
        """Returns a string representation of a message."""
        return self.countryName
   


class CountryTable(tables.Table):
    class Meta:
        model = Country
        template_name = "django_tables2/bootstrap.html"
        fields = ("countryName", "isLive", )

    # Select = tables.TemplateColumn('''
    #                                 <a href="/systems/{{ record.id }}">Select</a> 
    #                                 <a href="/schedule/delete_schedule/{{ record.id }}" 
    #                                     onclick="return confirm('Are you sure you want to delete this?')">on click test</a>''')
    


#Table Countries{
#  id integer [primary key]
#  countryName varchar
#  isLive bool [note:'is the country still operational']
#}