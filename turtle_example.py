from turtle import *
import turtle_shapes        # Import the modules

wn = Screen()               # Create a screen
wn.bgcolor('cyan')

# Create a turtle

cara = Turtle()
cara.shape('circle')
cara.up()

turtle_shapes.square(cara, 90)
cara.pu()
cara.fd(100)
turtle_shapes.tri(cara,150)
done()