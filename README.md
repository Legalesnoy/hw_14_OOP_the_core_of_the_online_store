# Домашняя работа по теме "Введение в ООП"

## Описание:

Учебное приложение на Python

Реализованы следующие классы ядра для интернет-магазина: 
- [Product](models/product.py) с описанием товара:
    - название (`name`) 
    - описание (`description`) 
    - цена (`price`) 
    - количество в наличии (`quantity`)
 
- [Category](models/category.py) с описанием категории: 
    - название (`name`)
    - описание (`description`)
    - список товаров категории (`products`) 
    - количество товаров (`product_count`)
    - количество категорий (`category_count`)
 
На основе класса **Product** реализованы классы:
- [LawnGrass](models/lawn_grass.py) - трава газонная, со свойствами:
    - страна-производитель (`country`)
    - срок прорастания (`germination_period`)
    - цвет (`color`)
- [Smartphone](models/smartphone.py) - смартфон, со свойствами:
    - производительность (`efficiency`)
    - модель (`model`)
    - объем встроенной памяти (`memory`)
    - цвет (`color`)
