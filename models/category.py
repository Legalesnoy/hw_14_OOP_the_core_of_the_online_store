from models.product import Product


class Category:
    name: str  # название
    description: str  # описание
    products: list[Product]  # список товаров категории

    product_count = 0  # количество товаров
    category_count = 0  # количество категорий
    __category_id: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        self.__category_id = Category.category_count
        Category.product_count += len(self.products)

    @property
    def category_id(self):
        return self.__category_id
