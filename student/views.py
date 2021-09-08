from django.shortcuts import render

# Create your views here.
def student_join(request):
    if request.method == "GET":
        render(request,"studentjoin.html",)