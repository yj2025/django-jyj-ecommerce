from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views, category_views

app_name = "api"
urlpatterns = [
    # path("hello-world/", base_views.hello_world),
    # path("hello-world-json/", base_views.hello_world_json),
    # path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29 proudct_view.py
    # http://127.0.0.1:8000/api/products/
    # 방식   url                 기능
    # GET  products/            list
    # POST products/            create
    # Get  product/{id}         product
    # PUT  product/{id}       modify product
    # DELETE  product/{id}    delete product
    path("products/", product_views.products_api),
    path("product/<int:pk>/", product_views.product_api),
    # dev_32
    # path("categories/", category_views.categories_api),
    # dev_35
    # 방식   url                  기능
    # GET  categories/           list
    # POST categories/           create
    # Get  category/{id}       category
    # PUT  category/{id}       modify category
    # DELETE  category/{id}    delete category
    # path("categories/", category_views.CategoriesAPI.as_view()),
    # path("category/<int:pk>/", category_views.CategoryAPI.as_view()),
    # dev_36
    path("categories/", category_views.CategoriesMixins.as_view()),
    path("category/<int:pk>/", category_views.CategoryMixins.as_view()),
]