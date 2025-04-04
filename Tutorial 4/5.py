class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ₹{self.salary}")

# Creating two instances of Person
p1 = Person("Alice", 30, 50000)
p2 = Person("Bob", 25, 45000)

p1.display()
p2.display()
