import turtle
t = turtle.Pen()

###The first thing we can do is use the .bgcolor() function on turtle to change the color of the canvas background! Try this now on the line below.
#Hint: In this case, we can't use out t variable because .bgcolor() doesn't work on the turtle Pen. Here we have to write out turtle.bgcolor("color")
#Here is a link to look up color names that work in Python: https://en.wikipedia.org/wiki/Web_colors





#What if you want to draw a dot with the circle filled in? There is a function for that called .dot("radius") that takes one parameter, which is radius in pixels.
#Draw a dot below with a radius of your choosing





#Use the dot and motion functions (forward, backward, left, right, etc.) to draw a shape with dots in each corner! Kind of like connect the dots.





#Is there a way to format the dimensions of your turtle? Yes there is!! Use the function .shapesize(length, width, outline width) to resize your turtle!





#What about pen width?? Use the function .pensize(thickness in pixels) to adjust the pen thickness




#Can I style my turtle further? Try using the .fillcolor("color") function to change the inner color of your turtle





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




#YOU CAN EVEN CHANGE YOUR TURTLE'S SHAPE! Use the .shape('type shape in here') function to set the turtle's shape. Your options are: Square, Arrow, Circle, Turtle,
Triangle, Classic






#Bonus Questions:


1)The eval() function takes in strings, converts them to integers or floats and then calculates the value of whatever the string was. For example


