import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(5,5,12)
ball.color("#53B8ED")
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0
ball.dx = 2


gravity = 0.1


while True:
    wn.update()
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Check for a wall collision
    if ball.xcor() > 375:
        ball.dx *= -1

    if ball.xcor() < -375:
        ball.dx *= -1 

    # Check for a bounce
    if ball.ycor() < -300:
        ball.dy *= -1











wn.mainloop()