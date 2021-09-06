from django.urls import path
from .views import add_course, add_batch, review_batch, home_view

urlpatterns=[
    path('',home_view, name="headmasterhome"),
    path('addcourse', add_course),
    path('addbatch', add_batch),
    path('reviewbatch', review_batch),

]