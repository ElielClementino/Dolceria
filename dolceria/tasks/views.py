# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import product_svc, todo_svc


@csrf_exempt
@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST["description"])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})


@ajax_login_required
def add_product(request):
    data = json.loads(request.body.decode())
    product = {
        "product": {
            "name": data["product"].get("name"),
            "image_url": data["product"].get("image_url"),
            "description": data["product"].get("description"),
            "quantity": data["product"].get("quantity"),
            "price": data["product"].get("price"),
        }
    }
    new_product = product_svc.add_product(product)
    return JsonResponse(new_product)


# @ajax_login_required
def list_products(request):
    products = product_svc.list_products()
    return JsonResponse({"products": products})
