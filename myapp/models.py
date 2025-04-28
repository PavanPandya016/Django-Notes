from django.db import models

# Create your models here.
class myapp_db(models.Model):
    topics = models.CharField(max_length = 100)
    notes = models.CharField(max_length = 500)
    time = models.TimeField()
    date = models.DateField()