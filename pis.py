class Pis:
    def __init__(self):
        self.products = {}
        self.count_id = 0
    
    def add(self, title, description):
        product = Product(self.count_id, title, description)
        self.products[self.count_id] = product
        self.count_id += 1

    def print_products(self):
        for product_id in self.products.keys():
            print(self.products[product_id])


class Product:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def __str__(self):
        return "ID: {}\nTitle: {}\nDescription: {}".format(
                self.id, self.title, self.description)
