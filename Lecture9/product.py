class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale
    

if __name__ == "__main__":
    apple1 = Product("Apple", 2.99)
    apple2 = apple1.product_on_sale()
    print(apple1)
    print(apple2)
    #print(apple1)