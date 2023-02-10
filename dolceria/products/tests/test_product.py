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
    response = client.post("/api/products/add/product", new_product)
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
        "/api/products/add/product", new_product, content_type="application/json"
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
    request = client.get("/api/products/list/products")
    response = request.json()

    assert request.status_code == 200
    assert len(response["products"]) == 4


def test_filter_products(user, client, db):
    client.force_login(user)
    baker.make(
        "Product",
        pk=1,
        name="Red Velvet",
        image_url="https://url.py",
        description="O Bolo Red Velvet é um bolo de textura muito leve e macia, levemente amanteigado e com um discreto sabor a chocolate. A sua massa é de cor vermelha, o que contrasta com o branco do creme queijo no recheio e cobertura-.",
        quantity=20,
        price=55.50,
    )
    baker.make(
        "Product",
        pk=2,
        name="Cenoura com calda de chocolate",
        image_url="https://url.py",
        description="O bolo de cenoura é um bolo doce com cenoura misturada dentro da massa.",
        quantity=10,
        price=65.50,
    )
    baker.make(
        "Product",
        pk=3,
        name="Morango com chantilly",
        image_url="https://url.py",
        description="A massa do bolo leva claras em neves, por isso fica bem leve e fofinha. Já o recheio é feito com leite condensado, creme de leite e morangos.",
        quantity=20,
        price=45.50,
    )
    chosen_products = [[{'id': 1, 'quantity': 6}], [{'id': 2, 'quantity': 3}]]
    request = client.post("/api/products/filter/products", chosen_products, content_type="application/json")
    response = request.json()


    assert request.status_code == 200
    assert len(response["products"]) == 2
