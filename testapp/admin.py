from django.contrib import admin
from testapp.models import User,ActivityPeriod


class UserAdmin(admin.ModelAdmin):
    list_display=['id','real_name','tz']

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display=['start_time','end_time']



# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(ActivityPeriod,ActivityPeriodAdmin)
