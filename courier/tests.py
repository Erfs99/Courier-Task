from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import CourierSerializer,DailySalarySerializer,WeeklySalarySerializer


class GetCouriers(APITestCase):
    client=APIClient()
    def setUp(self):
        CourierMan.objects.create(name='alAsi',last_name='s',mobile='23444432',national_id='42334234')


    def test_get_all_couriers(self):
        response=self.client.get('/')
        couriers=CourierMan.objects.all()
        serializer=CourierSerializer(couriers,many=True)
        self.assertEqual(len(serializer.data),len(response.data))
        self.assertEqual(response.status_code,status.HTTP_302_FOUND)



class GetDailySalaries(APITestCase):
    client=APIClient()
    def setUp(self):
        a=CourierMan.objects.create(name='a',last_name='b',mobile='23421443',national_id='42343423')
        DailySalary.objects.create(courier_man=a,date='2022-01-05',salary=0)
        

    def test_get_all_daily_salaries(self):
        response=self.client.get("/daily/")
        query=DailySalary.objects.all()
        serializer=DailySalarySerializer(query,many=True)
        self.assertEqual(len(response.data),len(serializer.data))
        self.assertEqual(response.status_code,status.HTTP_302_FOUND)




class GetWeeklySalaries(APITestCase):
    client=APIClient()
    def setUp(self):
        a=CourierMan.objects.create(name='c',last_name='g',mobile='234212443',national_id='423443423')
        WeeklySalary.objects.create(courier_man=a,from_date='2020-01-05',to_date='2022-01-09',salary=0)

    def test_get_all_weekly_salaries(self):
        response=self.client.get("/weekly/")
        query=WeeklySalary.objects.all()
        serializer=WeeklySalarySerializer(query,many=True)
        self.assertEqual(len(response.data),len(serializer.data))
        self.assertEqual(response.status_code,status.HTTP_302_FOUND)