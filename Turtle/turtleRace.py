import turtle, time, random

turtle.setup(1000, 1000)
ts = turtle.getscreen()

tim = turtle.Turtle()
tim.speed(1000)
tim.color('red')
tim.shape('turtle')
tim.pensize(5)

jeff = turtle.Turtle()
jeff.speed(1000)
jeff.color('purple')
jeff.shape('turtle')
jeff.pensize(5)

dave = turtle.Turtle()
dave.speed(1000)
dave.color('black')
dave.shape('turtle')
dave.pensize(5)

victor = turtle.Turtle()
victor.speed(1000)
victor.color('green')
victor.shape('turtle')
victor.pensize(5)

direction = [0, 0, 0, 0]
distance = [0, 0, 0, 0]


while True:
    for i in range(len(direction)):
        direction[i] = random.randrange(0, 360)

    for i in range(len(distance)):
        distance[i] = random.randrange(0, 10)

    tim.left(direction[0])
    jeff.left(direction[1])
    dave.left(direction[2])
    victor.left(direction[3])

    tim.forward(distance[0])
    jeff.forward(distance[1])
    dave.forward(distance[2])
    victor.forward(distance[3])

    if tim.ycor() >= 500 or tim.ycor() <= -500 or tim.xcor() >= 500 or tim.xcor() <= -500:
        tim.home()
        turtle.title("TIM WINS!")
    if jeff.ycor() >= 500 or jeff.ycor() <= -500 or jeff.xcor() >= 500 or jeff.xcor() <= -500:
        jeff.home()
        turtle.title("JEFF WINS!")
    if dave.ycor() >= 500 or dave.ycor() <= -500 or dave.xcor() >= 500 or dave.xcor() <= -500:
        dave.home()
        turtle.title("DAVE WINS!")
    if victor.ycor() >= 500 or victor.ycor() <= -500 or victor.xcor() >= 500 or victor.xcor() <= -500:
        victor.home()
        turtle.title("VICTOR WINS!")



