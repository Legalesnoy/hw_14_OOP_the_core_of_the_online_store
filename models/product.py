class Product:
    name: str  # название
    description: str  # описание
    __price: float  # цена
    quantity: int  # количество в наличии
    product_count = 0  # количество товаров в базе
    __product_id: int  # номер товара

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым или отрицательным количеством не может быть добавлен")
        self.__product_id = Product.product_count
        Product.product_count += 1

    @property
    def product_id(self):
        return self.__product_id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):

        if new_price > 0:

            if self.__price > new_price:
                if input("Понижаем цену? да - 'y', нет - 'n'\n") == 'y':
                    self.__price = round(new_price, 2)
            else:
                self.__price = round(new_price, 2)

        else:
            print(f"Стоиомость {self.name} не изменена. Цена '{new_price}'. "
                  f"Цена не должна быть нулевая или отрицательная.")

    def __repr__(self):
        return (f"номер товара: {self.product_id}\n"
                f"название: {self.name}\n"
                f"описание: {self.description}\n"
                f"цена: {self.__price}\n"
                f"количество в наличии: {self.quantity}\n"
                f"количество товаров в базе: {self.product_count}")

    @classmethod
    def new_product(cls, product: dict):
        return cls(**product)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.quantity * self.__price + other.quantity * other.__price


class Smartphone(Product):
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


class LawnGrass(Product):
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
