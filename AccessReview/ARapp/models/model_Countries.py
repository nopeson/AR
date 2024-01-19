from django.db import models
import datetime

class Country(models.Model):
    countryName = models.CharField(max_length=255)
    isLive = models.BooleanField()



#Table Countries{
#  id integer [primary key]
#  countryName varchar
#  isLive bool [note:'is the country still operational']
#}