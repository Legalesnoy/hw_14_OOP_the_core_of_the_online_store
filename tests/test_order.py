import pytest

from models.order import Order
from models.product import Product


@pytest.fixture()
def apple():
    return Product("Яблоко", "Голден", 59.99, 50)


def test_order_init(apple):
    order1 = Order.new_product(apple)
    assert order1.product.name == "Яблоко"
    assert order1.product.price == 59.99
    assert order1.product.quantity == 50
    assert order1.product.description == "Голден"


def test_order_new_product(apple):
    order1 = Order.new_product(apple)
    order1 = Order.new_product(apple)
    assert order1.product.name == "Яблоко"
    assert order1.product.price == 59.99
    assert order1.product.quantity == 50
    assert order1.product.description == "Голден"


def test_order_str(apple):
    order1 = Order.new_product(apple)
    assert order1.__str__() == "Куплен товар 'Яблоко', за 59.99 руб.,количество купленного товара 50 шт."
