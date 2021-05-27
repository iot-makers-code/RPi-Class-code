import turtle

len = 50
ang = 12
lv = 8

t = turtle.Turtle()
t.speed("fastest")
t.penup();t.lt(90);t.bk(len*1.7);t.pendown()
t.width(lv);t.fd(len)

def draw_tree(len, level):
    width = t.width()
    t.width(width * 3.0 / 4.0)
    len = 3.0 / 4.0 * len

    t.lt(ang);t.fd(len)
    if level < lv: draw_tree(len, level + 1)

    t.bk(len);t.rt(2 * ang);t.fd(len)
    if level < lv: draw_tree(len, level + 1)

    t.bk(len);t.lt(ang)
    t.width(width)

draw_tree(len, 2)
turtle.exitonclick()
