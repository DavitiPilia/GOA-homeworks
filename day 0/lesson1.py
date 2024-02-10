from turtle import *

speed(30)
#we want to paint a house

#step 1:draw a square
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of square

#drawing a door



forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()



color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()




#draw windows

penup()
color("blue")
begin_fill()
left(60)
forward(50)
right(30)
pendown()

forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
right(90)
forward(30)
right(90)
forward(115)
right(90)
forward(30)
pendown()
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()





exitonclick()