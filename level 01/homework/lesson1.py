from turtle import *


#making house

#drawe square
speed(200)    
width(7)
begin_fill()
color("purple")
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


#making door
forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



#making roof
penup()
goto(200,200)
pendown()
right(150)
begin_fill()
color("red")
forward(200)
left(120)
forward(200)
end_fill()


#making window 1
penup()
goto(10,120)
pendown()


begin_fill()
color("green")
left(120)
forward(45)
left(90)
forward(55)
left(90)
forward(45)
left(90)
forward(55)
end_fill()


# making window 2


penup()
goto(145,120)
pendown()
begin_fill()
left(90)
forward(45)
left(90)
forward(55)
left(90)
forward(45)
left(90)
forward(55)
end_fill()




exitonclick()