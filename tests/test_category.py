import pytest

from models.category import Category
from models.product import Product


@pytest.fixture()
def product_tablet():
    return Product("iPad Pro", "12.9-inch, 1TB, Wi-Fi + Cellular", 250000.0, 3)


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
    assert category_smartphone.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert category_smartphone.category_count == 1
    assert category_smartphone.category_id == 1
    assert category_smartphone.product_count == 1


def test_category_id(category_smartphone):
    assert category_smartphone.category_id == 2


def test_add_new_product(category_smartphone, product_tablet):
    initial_product_count = Category.product_count
    category_smartphone.add_product(product_tablet)

    assert "Ipad Pro" in category_smartphone.products
    assert Category.product_count == initial_product_count + 1


def test_add_existing_product(category_smartphone, product_smartphone):
    initial_product_count = Category.product_count
    updated_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 190000.0, 3)
    category_smartphone.add_product(updated_product)

    assert "Samsung Galaxy S23 Ultra, 190000.0 руб. Остаток: 8 шт." in category_smartphone.products
    assert Category.product_count == initial_product_count
