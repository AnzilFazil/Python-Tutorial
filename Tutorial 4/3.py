class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ₹{self.price}")

# Creating two instances of Car
car1 = Car("Toyota Camry", 2020, 2500000)
car2 = Car("Honda City", 2022, 1500000)

car1.cost()
car2.cost()
