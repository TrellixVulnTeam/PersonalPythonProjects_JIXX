import turtle
import time


tim = turtle.Turtle()
tim.speed(1)
tim.color('red')
tim.pensize(5)
tim.shape('turtle')

tim.forward(100)
tim.left(45)
tim.forward(100)
tim.right(90)
tim.forward(100)

tim.penup()
tim.backward(200)
tim.pendown()
tim.left(143)
tim.forward(100)
time.sleep(5)