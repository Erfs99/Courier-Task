from django.contrib import admin

# Register your models here.
from courier.models import *


class CourierManAdmin(admin.ModelAdmin):
    list_display=('name','last_name','mobile','national_id','salary')


class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display=('courier_man','status')

class DeliveryDetailsAdmin(admin.ModelAdmin):
    list_display=('courier_man','receiver','package_type','date')

class AddressAdmin(admin.ModelAdmin):
    list_display=('country','city','postcode')

class ReceiverAdmin(admin.ModelAdmin):
    list_display=('name','last_name','address')

class DailySalaryAdmin(admin.ModelAdmin):
    list_display=('courier_man','date','salary')

class WeeklySalaryAdmin(admin.ModelAdmin):
    list_display=('courier_man','from_date','to_date','salary')

admin.site.register(CourierMan,CourierManAdmin)
admin.site.register(DeliveryStatus,DeliveryStatusAdmin)
admin.site.register(DeliveryDetails,DeliveryDetailsAdmin)
admin.site.register(DailySalary,DailySalaryAdmin)
admin.site.register(WeeklySalary, WeeklySalaryAdmin)

