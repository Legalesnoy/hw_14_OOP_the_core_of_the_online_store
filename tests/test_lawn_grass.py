# test_lawn_grass.py
import pytest

from models.lawn_grass import LawnGrass
from models.product import Product


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


def test_lawn_grass(grass1):
    assert grass1.__str__() == ("Газонная трава, 500.0 руб. Остаток: 20 шт., "
                                "страна-производитель: Россия, "
                                "срок прорастания: 7 дней, "
                                "цвет: зеленый")


def test_lawn_grass_add(grass1, grass2):
    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0


@pytest.fixture()
def product_smartphone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 1000.0, 5)


def test_lawn_grass_add_error(grass1, product_smartphone):
    with pytest.raises(TypeError):
        _ = grass1 + 1

    with pytest.raises(TypeError):
        _ = grass1 + product_smartphone
