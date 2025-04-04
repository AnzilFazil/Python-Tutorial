class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

rect = Rectangle(l, w)
print("Area of Rectangle:", rect.area())
