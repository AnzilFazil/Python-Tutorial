def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    elif x == 0 and y != 0:
        return "On the Y-axis"
    elif y == 0 and x != 0:
        return "On the X-axis"
    elif x == 0 and y == 0:
        return "Origin"

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

result = find_quadrant(x, y)
print(f"The point ({x}, {y}) is in: {result}")
