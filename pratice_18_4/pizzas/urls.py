"""pizzas应用路由"""
from django.urls import path
from . import views

app_names = "pizzas"
urlpatterns = [
    # 主页
    path('',views.index,name="index"),
]