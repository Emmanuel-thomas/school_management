from django.shortcuts import render, redirect
from .forms import CourseAddForm, AddBatchForm


def add_course(request):
    context = {}
    if request.method == 'GET':
        form = CourseAddForm()
        context["form"] = form
        return render(request, "addcourse.html", context)
    elif request.method == 'POST':
        context = {}
        form = CourseAddForm(request.POST)
        context["form"] = form
        if form.is_valid():
            course_name = form.cleaned_data["course"]
            print(course_name)
            print("course added")
            return redirect("headmasterhome")


def add_batch(request):
    context = {}
    if request.method == 'GET':
        form = AddBatchForm()
        context["form"] = form
        return render(request, "addbatch.html", context)
    elif request.method == 'POST':
        print("hi")
        form = AddBatchForm(request.POST)
        if form.is_valid():
            batch_name = form.cleaned_data["batch_name"]
            starting_date = form.cleaned_data["starting_date"]
            course_name = form.cleaned_data["course_name"]
            print(batch_name, starting_date, course_name)

            return render(request, "headmaster/addbatch.html")
        else:
            print("form is not valid")
            return render(request, "headmaster/addbatch.html")


def review_batch(request):
    return render(request, "review_batch.html")


def home_view(request):
    return render(request, "headhome.html")
