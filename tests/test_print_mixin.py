from models.lawn_grass import LawnGrass
from models.product import Product
from models.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra",
            "256GB",
            180000.0,
            5)
    message1 = capsys.readouterr()
    assert message1.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB', 180000.0, 5)"

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    message2 = capsys.readouterr()
    assert message2.out.strip() == "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message3 = capsys.readouterr()
    assert message3.out.strip() == "LawnGrass('Газонная трава 2', 'Выносливая трава', 450.0, 15)"
