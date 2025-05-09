from models.base_product import BaseProduct
from models.product import Product


class Order(BaseProduct):
    """Класс «Заказ» содержит какой товар был куплен,
       В заказе может быть указан только один товар. """

    def __init__(self, product: Product, description: str = ''):
        self.product = product
        self.description = description

    def __str__(self):

        if self.description:
            comment = f"\nКомментарий к заказу: {self.description}"
        else:
            comment = ""
        return (f"Куплен товар '{self.product.name}', за {self.product.price} руб.,"
                f"количество купленного товара {self.product.quantity} шт.{comment}"
                )

    @classmethod
    def new_product(cls, product: Product):
        return cls(product)


if __name__ == "__main__":
    apple = Product("Яблоко", "Голден", 59.99, 50)
    order1 = Order.new_product(apple)
    order2 = Order(apple, "сплошная гниль, возврат")
    print(order2)
