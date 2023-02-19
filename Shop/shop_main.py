class Product:
    discount = 0.8

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price * self.quantity

    def get_discount_price(self):
        self.price = self.price - self.price * Product.discount
        return self.price


phone = Product("apple", 10000, 3)
print(phone.get_price())
phone.get_discount_price()
print(phone.price)
