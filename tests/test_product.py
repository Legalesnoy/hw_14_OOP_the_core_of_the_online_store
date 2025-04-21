# test_product.py
import pytest

from models.product import Product


@pytest.fixture()
def product_smartphone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 1000.0, 5)


def test_init(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 1000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.product_count == 1
    assert product_smartphone.product_id == 0


def test__repr__(product_smartphone):
    assert product_smartphone.__repr__() == ("номер товара: 1\n"
                                             "название: Samsung Galaxy S23 Ultra\n"
                                             "описание: 256GB, Серый цвет, 200MP камера\n"
                                             "цена: 1000.0\n"
                                             "количество в наличии: 5\n"
                                             "количество товаров в базе: 2")


def test_product_id(product_smartphone):
    assert product_smartphone.product_id == 2


def test_price_setter_increase(product_smartphone):
    product_smartphone.price = 1500
    assert product_smartphone.price == 1500


def test_price_setter_decrease_with_confirmation(mocker, product_smartphone):
    mocker.patch('builtins.input', return_value='y')
    product_smartphone.price = 800
    assert product_smartphone.price == 800


def test_price_setter_decrease_without_confirmation(mocker, product_smartphone):
    mocker.patch('builtins.input', return_value='n')
    product_smartphone.price = 800
    assert product_smartphone.price == 1000


def test_negative_price_setter(capsys, product_smartphone):
    product_smartphone.price = -500
    captured = capsys.readouterr()
    assert product_smartphone.price == 1000
    assert "Стоиомость Samsung Galaxy S23 Ultra не изменена. Цена '-500'."
    "Цена не должна быть нулевая или отрицательная." in captured.out


def test_new_product_from_dict():
    product_data = {
        "name": "Phone",
        "description": "Smartphone",
        "price": 700,
        "quantity": 10
    }
    product = Product.new_product(product_data)
    assert product.name == "Phone"
    assert product.price == 700
    assert product.quantity == 10


def test_negative_price_raises_error():
    with pytest.raises(ValueError) as exc_info:
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", -1000, 5)
    assert str(exc_info.value) == "Цена не должна быть нулевая или отрицательная"


def test_zero_quantity_raises_error():
    with pytest.raises(ValueError) as exc_info:
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 1000, 0)
    assert "Товар с нулевым или отрицательным количеством не может быть добавлен" in str(exc_info.value)
