from django.db import models

class R_ReviewType(models.Model):
    type = models.CharField(max_length=255)
    

# Table R_ReviewType{
#   id integer [primary key]
#   type varchar [note:'type of review - physical, AD review etc']
# }