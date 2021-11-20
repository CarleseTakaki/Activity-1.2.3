#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
writer= trtl.Turtle()
apple = trtl.Turtle()

#list of 5 apple turtles
all_apples = []
apple1 = trtl.Turtle()
all_apples.append(apple1)
apple2 = trtl.Turtle()
all_apples.append(apple2)
apple3 = trtl.Turtle()
all_apples.append(apple3)
apple4 = trtl.Turtle()
all_apples.append(apple4)
apple5 = trtl.Turtle()
all_apples.append(apple5)
#list of letter
letter_options = ["a", "s", "d", "f", "g"]


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

#drawing all of the apples
def draw_apple():
  apple1.shape(apple_image)
  apple1.penup()
  apple1.goto(-150,0)
  apple2.shape(apple_image)
  apple2.penup()
  apple2.goto(-75,-20)
  apple3.shape(apple_image)
  apple3.penup()
  apple3.goto(0,0)
  apple4.shape(apple_image)
  apple4.penup()
  apple4.goto(75,-20)
  apple5.shape(apple_image)
  apple5.penup()
  apple5.goto(150,0)

#defining where each apple turtle will go
def move_apple1():
  apple1.penup()
  apple_x1 = apple1.xcor()
  apple1.goto(apple_x1,-200)
  apple1.hideturtle()

def move_apple2():
  apple2.penup()
  apple_x2 = apple2.xcor()
  apple2.goto(apple_x2,-200)
  #writer.clear()
  apple2.hideturtle()

def move_apple3():
  apple3.penup()
  apple_x3 = apple3.xcor()
  apple3.goto(apple_x3,-200)
  #writer.clear()
  apple3.hideturtle()

def move_apple4():
  apple4.penup()
  apple_x4 = apple4.xcor()
  apple4.goto(apple_x4,-200)
  #writer.clear()
  apple4.hideturtle()

def move_apple5():
  apple5.penup()
  apple_x5 = apple5.xcor()
  apple5.goto(apple_x5,-200)
  #writer.clear()
  apple5.hideturtle()

#defing drawing each letter
def draw_letter1(apple):
  writer.penup()
  writer.hideturtle()
  writer.goto(-170,-30)
  writer.showturtle()
  writer.color("white")
  letter = letter_options[0]
  writer.write(letter, font=("Arial", 74, "bold"))

def draw_letter2(apple):
  writer.penup()
  writer.hideturtle()
  writer.goto(-95,-50)
  writer.showturtle()
  writer.color("white")
  letter = letter_options[1]
  writer.write(letter, font=("Arial", 74, "bold"))

def draw_letter3(apple):
  writer.penup()
  writer.hideturtle()
  writer.goto(-20,-30)
  writer.showturtle()
  writer.color("white")
  letter = letter_options[2]
  writer.write(letter, font=("Arial", 74, "bold"))

def draw_letter4(apple):
  writer.penup()
  writer.hideturtle()
  writer.goto(55,-50)
  writer.showturtle()
  writer.color("white")
  letter = letter_options[3]
  writer.write(letter, font=("Arial", 74, "bold"))

def draw_letter5(apple):
  writer.penup()
  writer.hideturtle()
  writer.goto(130,-30)
  writer.showturtle()
  writer.color("white")
  letter = letter_options[4]
  writer.write(letter, font=("Arial", 74, "bold"))

#-----function calls-----
wn.bgpic("background.gif")

#drawing all the apples 
draw_apple()
draw_letter1(apple)
draw_letter2(apple)
draw_letter3(apple)
draw_letter4(apple)
draw_letter5(apple)

#apple drops when ertian letter is clicked
wn.onkeypress(move_apple1, "a")
wn.onkeypress(move_apple2, "s")
wn.onkeypress(move_apple3, "d")
wn.onkeypress(move_apple4, "f")
wn.onkeypress(move_apple5, "g")
wn.listen()

wn.mainloop()
