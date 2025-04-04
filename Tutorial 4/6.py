class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0

    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

m1 = Mobile()

m1.set_details("Samsung", "Galaxy S21", 69999)

m1.display_details()
