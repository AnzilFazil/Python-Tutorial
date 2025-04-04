class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def find_center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of Rectangle
rect = Rectangle(10, 20, 0, 0)

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

center = rect.find_center()
print(f"Center: ({center[0]}, {center[1]})")
