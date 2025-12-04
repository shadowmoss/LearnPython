"""meal_plan_app的urls"""
from django.urls import path
from . import views

app_name = "meal_plan_app"
urlpatterns = [
    path('',views.index,name="index")
]