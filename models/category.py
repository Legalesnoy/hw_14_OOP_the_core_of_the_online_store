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
        for product in self.__products:
            if report != "":
                report += "\n"
            report += f'{product.name.title()}, {product.price} руб. Остаток: {product.quantity} шт.'
        return report
