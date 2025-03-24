class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price
    
    @property
    def name(self):
        return self.__name

    def __gt__(self, another_product):
        #return self.price > another_product.price
        return self.name > another_product.name
    

if __name__ == "__main__":
    orange = Product("Orange", 2.90)
    apple = Product("Apple", 3.95)

    if orange > apple:
        print("Orange is greater")
    else:
        print("Apple is greater")

    #number2 = []
    #print(dir(number2))

    #print(dir(Product))