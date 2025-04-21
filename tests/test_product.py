import pytest

from models.product import Product


@pytest.fixture()
def product_smartphone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.product_count == 3
    assert product_smartphone.product_id == 2


def test__repr__(product_smartphone):
    assert product_smartphone.__repr__() == ("номер товара: 3\n"
                                             "название: Samsung Galaxy S23 Ultra\n"
                                             "описание: 256GB, Серый цвет, 200MP камера\n"
                                             "цена: 180000.0\n"
                                             "количество в наличии: 5\n"
                                             "количество товаров в базе: 4")


def test_product_id(product_smartphone):
    assert product_smartphone.product_id == 4
