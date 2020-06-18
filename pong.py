import turtle

def create_window():
    window = turtle.Screen()
    window.title('Pong')
    window.bgcolor('black')
    window.setup(width=800,height=600)
    window.tracer(0)
    return window

def create_object(s,c,w,l,x,y):
    ob = turtle.Turtle()
    ob.speed(0)
    ob.shape(s)
    ob.color(c)
    ob.shapesize(stretch_wid=w,stretch_len=l)
    ob.penup()
    ob.goto(x,y)
    return ob

def paddle_left_change(distance):
    y =paddle_left.ycor()
    y += distance
    if y in range(-250,250):
        paddle_left.sety(y)
def paddle_left_up():
    paddle_left_change(20)
def paddle_left_down():
    paddle_left_change(-20)

def paddle_right_change(distance):
    y =paddle_right.ycor()
    y += distance
    if y in range(-250,250):
        paddle_right.sety(y)
def paddle_right_up():
    paddle_right_change(20)
def paddle_right_down():
    paddle_right_change(-20)

window = create_window()
paddle_left = create_object('square','red',5,1,-350,0)
paddle_right = create_object('square','blue',5,1,350,0)
ball = create_object('circle','white',1,1,0,0)

window.listen()
window.onkeypress(paddle_left_up,'w')
window.onkeypress(paddle_left_down,'s')
window.onkeypress(paddle_right_up,'Up')
window.onkeypress(paddle_right_down,'Down')

ball.dx = 0.25
ball.dy = -0.25

sp1 = 0
sp2 = 0

score_p1 = turtle.Turtle()
score_p1.speed(0)
score_p1.color('red')
score_p1.penup()
score_p1.hideturtle()
score_p1.setposition(-350,225)
score_p1.write('0', align='left',font=('Calibri',40,'normal'))

score_p2 = turtle.Turtle()
score_p2.speed(0)
score_p2.color('blue')
score_p2.penup()
score_p2.hideturtle()
score_p2.setposition(320,225)
score_p2.write('0', align='left',font=('Calibri',40,'normal'))

while True:
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        sp1+=1
        score_p1.clear()
        score_p1.write(sp1, align='left',font=('Calibri',40,'normal'))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        sp2+=1
        score_p2.clear()
        score_p2.write(sp2, align='left',font=('Calibri',40,'normal'))
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor()+60 and ball.ycor() > paddle_right.ycor()-60)):
        ball.setx(340)
        ball.dx *= -1
    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor()+60 and ball.ycor() > paddle_left.ycor()-60)):
        ball.setx(-340)
        ball.dx *= -1

# dodana linijka w nowym branchu