from dolceria.tasks.models import Product


def add_product(product):
    new_product = Product.objects.create(
        name=product["product"]["name"],
        image_url=product["product"]["image_url"],
        description=product["product"]["description"],
        quantity=product["product"]["quantity"],
        price=product["product"]["price"],
    )

    created_product = {
        "name": new_product.name,
        "image_url": new_product.image_url,
        "description": new_product.description,
        "quantity": new_product.quantity,
        "price": new_product.price,
    }

    return created_product


def list_products():
    products = Product.objects.all()
    breakpoint()
    return [product for product in products]
