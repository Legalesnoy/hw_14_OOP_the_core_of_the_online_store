class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    product_count = 0  # количество товаров в базе
    __product_id: int  # номер товара

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.__product_id = Product.product_count
        Product.product_count += 1

    @property
    def product_id(self):
        return self.__product_id

    def __repr__(self):
        return (f"номер товара: {self.product_id}\n"
                f"название: {self.name}\n"
                f"описание: {self.description}\n"
                f"цена: {self.price}\n"
                f"количество в наличии: {self.quantity}\n"
                f"количество товаров в базе: {self.product_count}")
