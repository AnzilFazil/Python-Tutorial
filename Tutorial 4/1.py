class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def read(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed."

a = Arith()
a.read()

print("Sum:", a.add())
print("Difference:", a.subtract())
print("Product:", a.multiply())
print("Quotient:", a.divide())
