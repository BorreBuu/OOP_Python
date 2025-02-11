class Product:
    def __init__(self, name: int, unit: str):
        self.name = name
        self.unit = unit


if __name__ == "__main__":
    shopping_list = []
    milk = Product("Milk", "litre")

    shopping_list.append(milk)
    shopping_list.append(milk)
    shopping_list.append(Product("Cucumber", "piece"))

    for item in shopping_list:
        print(item.name)

    shopping_list[0].name = "juice"

    for item in shopping_list:
        print(item.name)