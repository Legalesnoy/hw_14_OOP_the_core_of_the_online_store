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
        for prod in self.__products:
            if prod.name == new_product.name:
                prod.price = max(prod.price, new_product.price)
                prod.quantity += new_product.quantity
                return
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        return '\n'.join(str(prod) for prod in self.__products)

    def __str__(self):
        quantity = sum([prod.quantity for prod in self.__products])
        return f"{self.name}, количество продуктов: {quantity} шт."


class ProductIterator:
    """ класс для перебора продуктов в категории """
    index = 0
    category: Category

    def __init__(self, user_category):
        self.category = user_category

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        products = self.category.products.split('\n')
        if self.index < len(products):
            prod = products[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    # print(category1)
    # print(category1.category_id)
    # print('-'*50)
    product4 = Product("Iphone 15", "Фоновая подсветка", 12300000.0, 7)
    print(product4)
    print('* ' * 50)
    category1.add_product(product4)
    print(category1.products)
    print(' + ' * 20)
    pr = ProductIterator(category1)
    print(*(p for p in pr))

    # product5 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 1000000.0, 4)
    # category1.add_product(product4)
    # print(category1.products)
