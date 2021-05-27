from turtle import *
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(7)
def draw_circle(t, color, size, x, y):
  t.up();t.color(color); t.fillcolor(color);
  t.goto(x,y); t.down(); t.circle(size);
draw_circle(tommy,"green",50,25,0)
draw_circle(tommy,"blue",50,0,0)
draw_circle(tommy,"red",50,-25,0)
tommy.penup()
tommy.goto(0,-50)
tommy.color("orange")
tommy.write("Fun Code!",align="center"
              ,font=("Arial", 16, "bold"))
tommy.speed(10)
tommy.lt(90); tommy.fd(100); tommy.lt(90)
exitonclick()
