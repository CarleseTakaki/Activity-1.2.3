#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
apple = trtl.Turtle()
pear=trtl.Turtle()
writer= trtl.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_a()
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def move_apple(): 
  apple.penup()
  current_apple_x = apple.xcor()
  apple.goto(current_apple_x,-200)
  writer.clear()

def draw_a():
  writer.penup()
  writer.setposition(-40,-45)
  writer.color("white")
  writer.write("A", font=("Arial", 74, "bold"))

#-----function calls-----
draw_apple(apple)
wn.onkeypress(move_apple, "a")
#draw_pear(pear)
wn.bgpic("background.gif")
wn.listen()
wn.mainloop()
