import turtle
t = turtle.Turtle()
t.speed(0)

def draw_hexagon(size):
    """Draw a single hexagon."""
    for _ in range(6):
        t.forward(size)
        t.right(60)

for _ in range(10):
    draw_hexagon(50) 
    t.right(36) 

t.hideturtle()
turtle.done()
