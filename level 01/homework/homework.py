from turtle import *

speed(10)

width(7)
color("turquoise")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#End of square

#Drawing a door

forward(70)
color("magenta")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("gold")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#Drawing windows

#Left window
color("silver")
penup()
goto(0,200)
pendown()
begin_fill()

left(30)
left(90)
forward(65)
right(90)
forward(80)
right(90)
forward(65)
end_fill()

#Right window

penup()
goto(200,200)
pendown()
begin_fill()
forward(65)
left(90)
forward(80)
left(90)
forward(65)
end_fill()




exitonclick()