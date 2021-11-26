import turtle 

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')

t.speed(5)
col=['red','white','blue']
c = 0

for i in range(50):
    t.forward(i * 10)
    t.right(144)
    
    t.color(col[c])
    if c == 2:
        c = 0
    else:
        c = c + 1

s.exitonclick()
