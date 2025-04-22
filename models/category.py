from itertools import product

from models.product import Product


class Category:
    name: str  # название
    description: str  # описание
    __products: list[Product]  # список товаров категории

    product_count = 0  # количество товаров
    category_count = 0  # количество категорий
    __category_id: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        self.__category_id = Category.category_count
        Category.product_count += len(self.__products)

    @property
    def category_id(self):
        return self.__category_id

    def add_product(self, new_product: Product):
        for product in self.__products:
            if product.name == new_product.name:
                product.price = max(product.price, new_product.price)
                product.quantity = product.quantity + new_product.quantity
                return
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        report = ""
        for prod in self.__products:
            if report != "":
                report += "\n"
            report += prod.__
        return report

    def __str__(self):
        quantity = sum([prod.quantity for prod in self.__products])
        return f"{self.name.upper()}, количество продуктов: {quantity} шт."

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    print(category1)
