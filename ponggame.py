import turtle
import time
import random
score1=0
score2=0
game=True
delay=0.07
temp_direct1 = ""
temp_direct2 = ""
was_pause1 = ""
was_pause2 = ""
while game==True:
    ##restarting game
    score1 = 0
    score2 = 0
    temp_direct1 = ""
    temp_direct2 = ""
    was_pause1 = ""
    was_pause2 = ""
    text_endgame = turtle.Turtle()
    text_endgame.color("red")
    text_endgame.penup()
    text_endgame.goto(-40, 40)
    text_endgame.clear()
    text_endgame.hideturtle()
    ##creating the screen

    window=turtle.Screen()
    window.clear()
    window.bgcolor("black")
    window.setup(width=1000,height=600)
    window.tracer(0)
    window.title("pong game!")


    ##creating score player 2
    score_text2=turtle.Turtle()
    score_text2.color("white")
    score_text2.penup()
    score_text2.goto(-300,260)
    score_text2.write("player 2: "+str(score2),font=50)
    score_text2.hideturtle()

    ##creating score player 1
    score_text1 = turtle.Turtle()
    score_text1.color("white")
    score_text1.penup()
    score_text1.goto(230, 260)
    score_text1.write("player 1: " + str(score1), font=50)
    score_text1.hideturtle()

    ##creating a line in the middle
    line=turtle.Turtle()

    line.penup()
    line.pencolor("white")
    line.goto(0,300)
    line.pendown()
    line.goto(0,-300)
    line.hideturtle()



    ##creating the pedals
    ##player 1

    pedal1=turtle.Turtle()
    pedal1.color("white")
    pedal1.shape("square")
    pedal1.penup()
    pedal1.goto(480,0)

    pedal2 = turtle.Turtle()
    pedal2.color("white")
    pedal2.shape("square")
    pedal2.penup()
    pedal2.goto(480, 20)

    pedal3 = turtle.Turtle()
    pedal3.color("white")
    pedal3.shape("square")
    pedal3.penup()
    pedal3.goto(480, 40)

    pedal4 = turtle.Turtle()
    pedal4.color("white")
    pedal4.shape("square")
    pedal4.penup()
    pedal4.goto(480, -20)

    pedal5 = turtle.Turtle()
    pedal5.color("white")
    pedal5.shape("square")
    pedal5.penup()
    pedal5.goto(480, -40)

    ##player 2

    pedal6 = turtle.Turtle()
    pedal6.color("white")
    pedal6.shape("square")
    pedal6.penup()
    pedal6.goto(-485, 0)

    pedal7 = turtle.Turtle()
    pedal7.color("white")
    pedal7.shape("square")
    pedal7.penup()
    pedal7.goto(-485, 20)

    pedal8 = turtle.Turtle()
    pedal8.color("white")
    pedal8.shape("square")
    pedal8.penup()
    pedal8.goto(-485, 40)

    pedal9 = turtle.Turtle()
    pedal9.color("white")
    pedal9.shape("square")
    pedal9.penup()
    pedal9.goto(-485, -20)

    pedal10 = turtle.Turtle()
    pedal10.color("white")
    pedal10.shape("square")
    pedal10.penup()
    pedal10.goto(-485, -40)

    ##creating the ball
    ball=turtle.Turtle()
    ball.penup()
    ball.color("blue")
    ball.shape("circle")
    ball.shapesize(0.8,0.8,0.8)
    ball.goto(0,0)
    ball.dx=18
    ball.dy=18



    #functions
    def go_up1():
        if was_pause1!="pause":
            pedal1.direction="up"
        if was_pause1=="pause":
            if temp_direct1!="up":
                 pedal1.direction="up"


    def go_down1():
        if was_pause1 != "pause":
            pedal1.direction = "down"
        if was_pause1 == "pause":
            if temp_direct1 != "down":
                pedal1.direction = "down"



    def go_up2():
        if was_pause2 != "pause":
            pedal6.direction = "up"
        if was_pause2 == "pause":
            if temp_direct2 != "up":
                pedal6.direction = "up"


    def go_down2():
        if was_pause2 != "pause":
            pedal6.direction = "down"
        if was_pause2 == "pause":
            if temp_direct2 != "down":
                pedal6.direction = "down"






    def move():
        if pedal1.direction=="up":

            pedal1.sety(pedal1.ycor()+20)
            pedal2.sety(pedal2.ycor() + 20)
            pedal3.sety(pedal3.ycor() + 20)
            pedal4.sety(pedal4.ycor() + 20)
            pedal5.sety(pedal5.ycor() + 20)


        if pedal1.direction=="down":
            pedal1.sety(pedal1.ycor() - 20)
            pedal2.sety(pedal2.ycor() - 20)
            pedal3.sety(pedal3.ycor() - 20)
            pedal4.sety(pedal4.ycor() - 20)
            pedal5.sety(pedal5.ycor() - 20)


        if pedal6.direction == "up":
            pedal6.sety(pedal6.ycor() + 20)
            pedal7.sety(pedal7.ycor() + 20)
            pedal8.sety(pedal8.ycor() + 20)
            pedal9.sety(pedal9.ycor() + 20)
            pedal10.sety(pedal10.ycor() + 20)


        if pedal6.direction == "down":
            pedal6.sety(pedal6.ycor() -20)
            pedal7.sety(pedal7.ycor() - 20)
            pedal8.sety(pedal8.ycor() - 20)
            pedal9.sety(pedal9.ycor() - 20)
            pedal10.sety(pedal10.ycor() - 20)



    def pause1():
            pedal1.direction="stop"
            pedal2.direction = "stop"
            pedal3.direction = "stop"
            pedal4.direction = "stop"
            pedal5.direction = "stop"

    def pause2():
            pedal6.direction="stop"
            pedal7.direction = "stop"
            pedal8.direction = "stop"
            pedal9.direction = "stop"
            pedal10.direction = "stop"

    def byebye():
        game=False
        window.bye()





    #keybindings
    window.listen()
    window.onkeypress(go_up1,'9')
    window.onkeypress(go_down1,'6')
    window.onkeypress(go_up2, 'w')
    window.onkeypress(go_down2, 's')

    while score1<7 and score2<7:
        window.update()
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        ##border check
        if ball.ycor()>290:

            ball.dy*=-1
        if ball.ycor()<-290:

            ball.dy *= -1
        ##pedal hitting the ball
        if pedal1.distance(ball)<20 or pedal2.distance(ball)<20 or pedal3.distance(ball)<20 or pedal4.distance(ball)<20 or pedal5.distance(ball)<20 or pedal6.distance(ball)<20 or pedal7.distance(ball)<20 or pedal8.distance(ball)<20 or pedal9.distance(ball)<20 or pedal10.distance(ball)<20:
            ball.dx*=-1
        ##score for player 2
        if ball.xcor()>520:
            score2+=1
            time.sleep(1)
            score_text2.clear()
            score_text2.write("player 2: " + str(score2), font=50)
            ball.goto(0,random.randint(-250,250))

        ##score for player 1
        if ball.xcor()<-530:
            score1+=1
            time.sleep(1)
            score_text1.clear()
            score_text1.write("player 1: " + str(score1), font=50)
            ball.goto(0, random.randint(-250, 250))

        move()
        was_pause1=""
        was_pause2=""
        if pedal3.ycor()==300 or pedal5.ycor()==-280:
            if pedal1.direction != "stop":
                temp_direct1 = pedal1.direction
            pause1()
            was_pause1="pause"
        if pedal8.ycor()==300 or pedal10.ycor()==-280:
            if pedal6.direction != "stop":
                temp_direct2 = pedal6.direction
            pause2()
            was_pause2="pause"

        time.sleep(delay)
    text_endgame=turtle.Turtle()
    text_endgame.color("red")
    text_endgame.penup()
    text_endgame.goto(-40,40)
    if score1==7:
        text_endgame.write("game ended! player 1 won!",font=15)
    if score2==7:
        text_endgame.write("game ended! player 2 won!",font=15)
    text_endgame.hideturtle()
    time.sleep(3)
    text_endgame.clear()
    text_endgame.write("do you want to play again? click n if not",font=15)
    window.listen()
    window.onkeypress(byebye,'n')
    time.sleep(5)















window.mainloop()