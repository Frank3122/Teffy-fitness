from website.views import *
from django.urls import path,include

urlpatterns = [
    path("home/",home,name="home"),
    path("method/", method, name="method"),
    path("test/", test, name="test"),
    path("story/", story, name="story"),
    path("sports/", sports, name="sports"),
    path("fitness/", fitness, name="fitness"),
    path("academy/", academy, name="academy"),
    path("events/", events, name="events"),
    path("forms/", forms, name="forms"),
    path("gymform/", gymform, name="gymform"),

]