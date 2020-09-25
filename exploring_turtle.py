###Remember, any time you want to reset your canvas, you can type out t.reset(). Use t.clear() if you want to leave your turtle where it is###
import turtle
t = turtle.Pen()

###The first thing we can do is use the .bgcolor() function on turtle to change the color of the canvas background! Try this now on the line below.
#Hint: In this case, we can't use our t variable because .bgcolor() doesn't work on the turtle Pen. Here we have to write out turtle.bgcolor("color")
#Here is a link to look up color names that work in Python: https://en.wikipedia.org/wiki/Web_colors





#What if you want to draw a dot with the circle filled in? There is a function for that called .dot("radius") that takes one parameter, which is radius in pixels.
#Draw a dot below with a radius of your choosing





#Use the dot and motion functions (forward, backward, left, right, etc.) to draw a shape with dots in each corner! Kind of like connect the dots.





#Is there a way to format the dimensions of your turtle? Yes there is!! Use the function .shapesize(length, width, outline width) to resize your turtle!





#What about pen width?? Use the function .pensize(thickness in pixels) to adjust the pen thickness




#Can I style my turtle further? Try using the .fillcolor("color") function to change the inner color of your turtle




#YOU CAN EVEN CHANGE YOUR TURTLE'S SHAPE! Use the .shape('type shape in here') function to set the turtle's shape. Your options are: Square, Arrow, Circle, Turtle,
#Triangle, Classic




#Guess what else? You could have made most of these alterations to your turtle in one line of code
#e.g. t.pen(pencolor="yellow", fillcolor="blue", pensize=10, speed=1) ->Try it below!!




#Filling a custom image: Use the .begin_fill() and end_fill() functions around action commands to fill a shape once it is completed. There is an example below:
'''
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()
'''
#Create a custom shape and fill it in using the .begin_fill() and end_fill() functions!








#-----------------------------------------------------------------------------------------#

#Bonus Questions:


# 1)Review Question: There are three new functions that can help you with this bonus math problem. str() converts whatever is inside it's parentheses to a string data type.
#The float() function converts whatever is in the parentheses into a float, and the int() function converts whatever is in the parentheses into an integer.
#e.g. print(str(4.57893)) would print the string '4.57893'

#You are helping your friend order some pizza. Your friend is looking at the menu and telling you how many pizzas they want, as well as the cost of the pizza. The
#pizza has a sales tax of 8%(.08). Follow the prompts in order to determine how much your order will cost (Hint: You may need to use the input function as well!):


#a) First ask your friend how many pizzas they want to order and store that as variable num_pizzas


#b)Then ask your friend how much each pizza costs and store that as a variable pizza_cost


#c)Calculate the total cost of your pizzas before tax and store that as variable subtotal_pizza


#d)Calculate the sales tax owed on your order and store that as variable sales_tax
tax_rate = 0.08


#e)Add the sales tax to your order subtotal and store that as variable total


#f) Tell your friend how much the entire order will cost using the variable total in your print statement (make sure you write out a message and use + to add
#strings together in your print statement




#2)Take a potential answer to the last assignment's spiral bonus question:
'''
t.reset()
colors = ["red", "yellow", "blue", "green"] 
for x in range(100):
  t.pencolor(colors[x%4]) t.forward(x)
  t.left(91)
'''
#Instead of drawing a coninuous line, could you add steps in here to make it a dashed line? What if you want to write your name over and over again in a 
#spiral-like pattern? What if you wanted your name to increase in size each time you wrote it? Hint: Look up the .write() function for turtle and see what
#parameters it takes. See if you can incorporate it into your program!








