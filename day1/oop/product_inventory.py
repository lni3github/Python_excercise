class Product:
    def __init__(self, name, product_id, price:int):
        self.name = name
        self.product_id = product_id
        self.price = price

class Inventory:
    def __init__(self):
        self.products = {}

    def add(self, product_obj):
        self.products[product_obj.product_id] = product_obj

    def remove(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            self.list()
        else:
            print("product not found")

    def list(self):
        products_json = []
        for product in self.products.values():
            products_json.append(f"product_id: {product.product_id}, name: {product.name}, price: {product.price}")
        print(products_json)


product1 = Product("Hamberger", "001", 500)
product2 = Product("BigHamberger", "002", 900)

inventory = Inventory()
inventory.add(product1)
inventory.add(product2)
inventory.remove("002")
