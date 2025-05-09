from models.product import Product


class LawnGrass(Product):
    """класс Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f'{super().__str__()}, '
                f'страна-производитель: {self.country}, '
                f'срок прорастания: {self.germination_period}, '
                f'цвет: {self.color.lower()}')
