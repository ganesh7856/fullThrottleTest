
from testapp.models import User, ActivityPeriod
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
'''
def UserJasonAPI(request):
   UserData=User.objects.all()
   User_Info={'id':UserData.id,
   'real_name':UserData.real_name,
   'tz':UserData.tz,
   'start_time':UserData.start_time,
   'end_time':UserData.start_time}
   return JsonResponse(User,safe=False)

   '''


def UserJasonAPI(request):
   queryset=User.objects.all()
   queryset=serializers.serialize('json',queryset)
   return HttpResponse(queryset,content_type='application/json')

def ActivityPeriodJasonAPI(request):
      queryset_activites=ActivityPeriod.objects.all()
      queryset_activites=serializers.serialize('json',queryset_activites)
      return HttpResponse(queryset_activites,content_type='application/json')
