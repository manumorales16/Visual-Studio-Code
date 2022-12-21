import turtle

# Crea una tortuga y configura su tamaño y color
t = turtle.Turtle()
t.pensize(5)
t.color("red")

# Dibuja un círculo para el emblema
t.circle(100)

# Dibuja las rayas del emblema
t.penup()
t.goto(-40, 100)
t.pendown()
t.goto(40, 100)

t.penup()
t.goto(100, 40)
t.pendown()
t.goto(100, -40)

t.penup()
t.goto(40, -100)
t.pendown()
t.goto(-40, -100)

t.penup()
t.goto(-100, -40)
t.pendown()
t.goto(-100, 40)

# Muestra el dibujo
turtle.done()
