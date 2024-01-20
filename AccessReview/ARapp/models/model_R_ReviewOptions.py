from django.db import models
import datetime

class R_ReviewResponseOptions(models.Model):
    response = models.CharField(max_length=255)
    
    def __str__(self):
        """Returns a string representation of a message."""
        return self.response





# /*
# Table R_ReviewResponseOptions{
#   id integer [primary key]
#   response varchar

# }
# */