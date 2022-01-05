from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .api_views import CourierView,DailyView,WeeklyView
urlpatterns = [
    path('',CourierView.as_view()),
    path('daily/',DailyView.as_view()),
    path('weekly/',WeeklyView.as_view())

]
