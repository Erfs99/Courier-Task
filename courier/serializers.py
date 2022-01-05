from rest_framework import serializers
from .models import *

class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourierMan
        fields = '__all__'


class DailySalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = DailySalary
        fields = '__all__'


class WeeklySalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeeklySalary
        fields = '__all__'