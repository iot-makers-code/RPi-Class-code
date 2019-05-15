from turtle import *
bgcolor('black')
colors=['red','purple','blue', 'green','yellow','orange']

for i in range(180):
    pencolor(colors[i % 6])
    forward(i)
    left(61)
exitonclick()
