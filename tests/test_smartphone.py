# test_smartphone.py
import pytest

from models.smartphone import Smartphone


@pytest.fixture()
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


def test_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.product_count == 36
    assert smartphone1.product_id == 35


def test__str__(smartphone1):
    assert str(smartphone1) == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. производительность: '
                                '95.5, модель: S23 Ultra, объем встроенной памяти: 256, цвет: Серый')
