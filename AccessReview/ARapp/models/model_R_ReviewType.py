from django.db import models

class R_ReviewType(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self):
        """Returns a string representation of a message."""
        return self.type
    


# Table R_ReviewType{
#   id integer [primary key]
#   type varchar [note:'type of review - physical, AD review etc']
# }