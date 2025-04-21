import pytest

from models.category import Category
from models.product import Product


@pytest.fixture()
def product_smartphone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def category_smartphone(product_smartphone):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                    "функций для удобства жизни",
                    [product_smartphone])


def test_init(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == ("Смартфоны, как средство не только коммуникации, "
                                               "но и получения дополнительных функций для удобства жизни")
    assert str(category_smartphone.products[0]) == ("номер товара: 0\n"
                                                    "название: Samsung Galaxy S23 Ultra\n"
                                                    "описание: 256GB, Серый цвет, 200MP камера\n"
                                                    "цена: 180000.0\n"
                                                    "количество в наличии: 5\n"
                                                    "количество товаров в базе: 1")
    assert category_smartphone.category_count == 1
    assert category_smartphone.category_id == 1
    assert category_smartphone.product_count == 1


def test_category_id(category_smartphone):
    assert category_smartphone.category_id == 2
