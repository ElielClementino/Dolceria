from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
    path("add/product", views.add_product),
    path("list/products", views.list_products),
]
