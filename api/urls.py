from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# dev_28
from api.views import hello_world, hello_world_drf, hello_world_json

app_name = "api"
urlpatterns = [
    path("hellow-world/", hello_world),
    path("hellow-world-json/", hello_world_json),
    path("hellow-world-drf/", hello_world_drf),
]