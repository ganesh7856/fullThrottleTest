import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FullThrottle.settings')
import django
django.setup()


from testapp.models import *
from faker import Faker
from random import *
from django.utils import timezone

faker=Faker()

def dummydata(n):
    for i in range(n):
        id=randint(101,211)
        real_name=faker.name()
        tz=faker.city()
        user_records=User.objects.get_or_create(id=id,real_name=real_name,tz=tz)

dummydata(20)


        #def activitydummy():
            #start_time=models.DateTimeField(auto_now_add=True)
            #end_time=models.DateTimeField(auto_now_add=True)
            #ActivityPeriod_records=ActivityPeriod.objects.get_or_create(start_time=start_time,end_time=end_time)
        #activitydummy(1)
