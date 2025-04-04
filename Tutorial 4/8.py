class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0.0

    def get_details(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author name: ")
        self.cost = float(input("Enter book cost: "))

    def print_details(self):
        print("\n--- Book Details ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost: ₹{self.cost}")

b = Book()
b.get_details()
b.print_details()
