from django.shortcuts import render
from django.http import HttpResponse

# view of localhost/home/
def home(request):
    return HttpResponse("<h1> Blog home </h1>")


# view of localhost/home/about/
def about(request):
    return HttpResponse("<h1> About blog</h1>")
