from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def follow_ups(request):
    return HttpResponse("<h1>follow up done<h1>")


def class_test(request):
    return HttpResponse("<h1> test completed")

