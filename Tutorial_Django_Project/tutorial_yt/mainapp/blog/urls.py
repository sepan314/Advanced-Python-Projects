from django.urls import path
from . import views

# url redirects path('path_name', function name, name)
urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
