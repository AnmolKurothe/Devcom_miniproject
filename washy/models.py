from django.db import models

# Create your models here.
class washingmachine(models.Model):
    name = models.CharField(max_length=50)
    # Wing = models.CharField(max_length=50)
    room_no = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()



    