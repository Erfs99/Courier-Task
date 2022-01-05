from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CourierSerializer,DailySalarySerializer,WeeklySalary, WeeklySalarySerializer
from .models import CourierMan,DailySalary,WeeklySalary
from rest_framework import status



class CourierView(APIView):
    """
    view represents today couriers salary
    """

    serializer_class=CourierSerializer
    def get(self,request):
        queryset=CourierMan.objects.all()
        serializer=self.serializer_class(queryset,many=True)
        return Response({'data':serializer.data},status=status.HTTP_302_FOUND)
        

class DailyView(APIView):
    """
    view represents couriers salary on different days
    """

    serializer_class=DailySalarySerializer
    def get(self,request):
        queryset=DailySalary.objects.all()
        serializer=self.serializer_class(queryset,many=True)
        return Response({'data':serializer.data},status= status.HTTP_302_FOUND)


class WeeklyView(APIView):
    """
    view represents weekly salary
    """
    serializer_class=WeeklySalarySerializer
    def get(self,request):
        queryset=WeeklySalary.objects.all()
        serializer=self.serializer_class(queryset,many=True)
        return Response({'data':serializer.data},status= status.HTTP_302_FOUND)
