from __future__ import unicode_literals,absolute_import
from celery import shared_task
from .models import DeliveryDetails,CourierMan,DailySalary,WeeklySalary
import datetime
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import ExtractWeek

@shared_task
def CalculateDailySalary():
    """Calculates Couriers Daily Salary at the end of the day 
    and saves them, starts the next day with 0 value """
    queryset=CourierMan.objects.all()
    for courier in queryset:
        value=courier.salary
        DailySalary.objects.create(courier_man=courier,date=datetime.date.today(),salary=value)
        courier.salary = 0
        courier.save()

@shared_task
def CalculateWeeklySalary():
    """runs each week and calculates sum of last 7 days salary of couriers
    and saves them in weeklysalary"""
    today = timezone.now().date()
    last_week = timezone.now().date() - timedelta(days=7)
    queryset = CourierMan.objects.all()
    for courier in queryset:
        result = DailySalary.objects.filter(date__gte=last_week,courier_man=courier).annotate(week=ExtractWeek('date')).values('courier_man','week').annotate(week_total=Sum('salary')).order_by('week')
        for i in result:
            WeeklySalary.objects.create(courier_man_id=i['courier_man'],from_date=last_week,to_date=today,salary=i['week_total'])



