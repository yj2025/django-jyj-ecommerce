from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views

app_name = "api"
urlpatterns = [
    path("hello-world/", base_views.hello_world),
    path("hello-world-json/", base_views.hello_world_json),
    path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29 proudct_view.py
    #http://127.0.0.1:8000/api/products/
    path("products/", product_views.products_api),
]