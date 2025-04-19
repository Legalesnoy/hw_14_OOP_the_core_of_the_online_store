class Product:
    __product_id: int # номер товара
    name: str # название
    description: str # описание
    price: float # цена
    quantity: int # количество в наличии
    product_count = 0 # количество товаров в базе

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1
        self.__product_id = Product.product_count


    @property
    def product_id(self):
        return self.__product_id

    def __repr__(self):
        return (f"номер товара: {self.product_id}\n"
                f"название: {self.name}\n"
                f"описание: {self.description}\n"
                f"цена: {self.price}\n"
                f"количество в наличии: {self.quantity}\n"
                f"количество товаров в базе {self.product_count}")


class Category:
    name: str # название
    description: str # описание
    products:list[Product] # список товаров категории

    product_count = 0 # количество товаров
    category_count = 0 # количество категорий
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





if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
    print(Product.product_count)