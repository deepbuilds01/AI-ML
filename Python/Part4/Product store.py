class Product:
    count = 0
    def __init__(self, name,price):
        self.name = name
        self.price = price
        Product.count +=1


    #  Instance methode
    def get_info(self):
        print(f"The Product name is {self.name} and Price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f" The tortal count is {cls.count}")


    


p1 = Product("Mac",50_000)
p1 = Product("Mac",50_000)
p1 = Product("Mac",50_000)
p1 = Product("Mac",50_000)
p1 = Product("Mac",50_000)
p1 = Product("Mac",50_000)

p1.get_info()
Product.get_count()