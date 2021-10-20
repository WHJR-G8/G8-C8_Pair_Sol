import turtle

def position(x,y,c): #Function used to move turtle to various positions and fill colors
    turtle.penup() #Pull the pen up
    turtle.goto(x,y) #Move turtle to a specified position
    turtle.pendown() #Pull the pen down
    turtle.fillcolor(c) #Specify the color to be filled
    turtle.begin_fill() #Begin the color fill
    
def draw_rect(s1,s2): #Function used to draw rectangles
    for i in range(2):
        turtle.forward(s1)
        turtle.right(90)
        turtle.forward(s2)
        turtle.right(90)
    
    turtle.end_fill() #End the color filling

#Student 1

position(10,-10,"red") #Function call to start the color filling for the upper portion i.e. triangle and move the turtle to the position (10, -10)

for i in range(3): #Draw the triangle
    turtle.forward(100)
    turtle.left(120)
    
turtle.end_fill()

position(85,-40,"blue") #Function call to start the color filling for the right side rectangle and move the turtle to the position (85, -40)

draw_rect(40,150) #Function call to draw the right side rectangle

#Student 2

position(10,-10,"green") #Function call to start the color filling for the middle rectangle and move the turtle to the position (10, -10)

draw_rect(100,150) #Function call to draw the middle rectangle

position(-5,-40,"blue") #Function call to start the color filling for the left side rectangle and move the turtle to the position (-5, -40)

draw_rect(40,150) #Function call to draw the left side rectangle

turtle.ht() #Used to hide the turtle/pen
