from django.urls import path
from .views import follow_ups, class_test
from django.shortcuts import render




urlpatterns=[
    path('',lambda request: render(request,"teacherhome.html"), ),
    path("followups/", follow_ups),
    path("classtest/", class_test),

]