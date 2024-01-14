from django.db import models
import datetime

class Systems(models.Model):
    systemName = models.CharField(max_length=255)
    criticality = models.CharField(max_length=255)


#Table Systems{
#  id integer [primary key]
#  systemName varchar
#  criticality varchar
#  accessMatrix_ID integer [ref: - AccessMatrixList.id]
#  country_ID integer [ref: > Countries.id]
#  lastReviewedOn timestamp
#  assetOwner_ID integer [ref: - Users.employee_ID]
#}