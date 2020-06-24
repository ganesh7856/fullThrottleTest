from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=250,primary_key=True)
    real_name=models.CharField(max_length=250)
    tz=models.CharField(max_length=250)

    def __str__(self):
            return self.real_name

class ActivityPeriod(models.Model):
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
