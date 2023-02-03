from model_bakery import baker

from dolceria.accounts.tests import fixtures


def test_add_product_without_being_logged(client):
    new_product = {
        "product": {
            "name": "Red Velvet",
            "image_url": "https://url.py",
            "description": "O Bolo Red Velvet é um bolo de textura muito leve e macia, levemente amanteigado e com um discreto sabor a chocolate. A sua massa é de cor vermelha, o que contrasta com o branco do creme queijo no recheio e cobertura-.",
            "quantity": 30,
            "price": 55.50,
        }
    }
    response = client.post("/api/tasks/add/product", new_product)
    assert response.status_code == 401


def test_if_product_is_being_created(user, client, db):
    client.force_login(user)

    product = baker.make(
        "Product",
        name="Red Velvet",
        image_url="https://url.py",
        description="O Bolo Red Velvet é um bolo de textura muito leve e macia, levemente amanteigado e com um discreto sabor a chocolate. A sua massa é de cor vermelha, o que contrasta com o branco do creme queijo no recheio e cobertura-.",
        quantity=30,
        price=55.50,
    )
    new_product = {
        "product": {
            "name": product.name,
            "image_url": product.image_url,
            "description": product.description,
            "quantity": product.quantity,
            "price": product.price,
        }
    }

    request = client.post(
        "/api/tasks/add/product", new_product, content_type="application/json"
    )
    response = request.json()

    assert request.status_code == 200
    assert response["name"] == product.name
    assert response["image_url"] == product.image_url
    assert response["description"] == product.description
    assert response["quantity"] == product.quantity
    assert response["price"] == product.price


def test_list_all_products(user, client, db):
    client.force_login(user)
    # esse "_quantity" no baker é diferente do "quantity", o "quantity" é um campo no modelo, enquanto o "_quantity" é um parâmetro que o baker aceita para criar mais de 1 objeto, assim não tenho que repetir essa linha mais de 1 vez.
    baker.make(
        "Product",
        name="Red Velvet",
        image_url="https://url.py",
        description="O Bolo Red Velvet é um bolo de textura muito leve e macia, levemente amanteigado e com um discreto sabor a chocolate. A sua massa é de cor vermelha, o que contrasta com o branco do creme queijo no recheio e cobertura-.",
        quantity=30,
        price=55.50,
        _quantity=4,
    )
    request = client.get("/api/tasks/list/products")
    response = request.json()

    assert request.status_code == 200
    assert len(response["products"]) == 4
