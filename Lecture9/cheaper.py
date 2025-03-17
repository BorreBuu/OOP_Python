class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def cheaper(self, Product):
        if self.__price < Product.price:
            return self
        else:
            return Product
        

apple = Product("Apple", 2.99)
orange = Product("Orange", 3.95)
banana = Product("Banana", 5.25)

print(orange.cheaper(apple))
print(orange.cheaper(banana))