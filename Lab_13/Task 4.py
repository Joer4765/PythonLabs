class Product:
    def __init__(self, name, price, category, weight):
        self.data = (name, price, category, weight)

    def get_all_values(self):
        return self.data

    def get_value(self, index):
        return self.data[index]


def social_products(products):
    average_price = sum([product.get_value(1) for product in products]) / len(products)
    social_products = [product for product in products if product.get_value(1) < average_price]
    return len(social_products)


# Створення продуктів
product1 = Product('Яблуко', 10, 'Фрукти', 0.2)
product2 = Product('Банан', 15, 'Фрукти', 0.3)
product3 = Product('Молоко', 25, 'Молочні продукти', 1.0)

# Список продуктів
products = [product1, product2, product3]

# Виведення кількості продуктів соціальної категорії
print(social_products(products))
