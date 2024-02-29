import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(2)
tur.width(10)
tur.bgcolor("brown")
for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(80,24)
        tur.hideturtle()
        tur.done()