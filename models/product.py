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
