from models.product import Product


class Smartphone(Product):
    """ класс смартфон"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f'{super().__str__()} '
                f'производительность: {self.efficiency}, '
                f'модель: {self.model}, '
                f'объем встроенной памяти: {self.memory}, '
                f'цвет: {self.color}')
