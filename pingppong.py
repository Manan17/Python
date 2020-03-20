import turtle

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("Black")
wn.setup(width = 800, height = 600)
#wn.bgpic("background.gif")
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

#Player A
playerA = turtle.Turtle()
playerA.shape("square")
playerA.speed(0)
playerA.shapesize(stretch_wid=5,stretch_len=1)
playerA.penup()
playerA.color("white")
playerA.goto(-350,0)


#Player B
playerB = turtle.Turtle()
playerB.shape("square")
playerB.speed(0)
playerB.shapesize(stretch_wid=5,stretch_len=1)
playerB.penup()
playerB.color("white")
playerB.goto(350,0)

#Ball
gameBall = turtle.Turtle()
gameBall.shape("circle")
gameBall.speed(0)
gameBall.penup()
gameBall.color("white")
gameBall.goto(0,0)
gameBall.dx = 0.2
gameBall.dy = 0.2

#ScorePen
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.penup()
scorePen.color("white")
scorePen.hideturtle()
scorePen.goto(0,260)
scorePen.write("Player A : 0     Player B : 0" , align= "center",font=("Arial",20,"bold"))



#Movement of Paddle A
def playerAUp():
    y = playerA.ycor()
    if y < 232:
        y+=20
        playerA.sety(y)

def playerADown():
    y = playerA.ycor()
    if y > -222:
        y-=20
        playerA.sety(y)

#Movement of Paddle B
def playerBUp():
    y = playerB.ycor()
    if y < 232:    
        y+=20
        playerB.sety(y)

def playerBDown():
    y = playerB.ycor()
    if y > -222:
        y-=20
        playerB.sety(y)


#Keyboard Listening
wn.listen()
wn.onkeypress(playerAUp,"w")
wn.onkeypress(playerADown,"s")
wn.onkeypress(playerBUp,"Up")
wn.onkeypress(playerBDown,"Down")

#Main Loop
while True:
    wn.update()
    #Moving the ball
    gameBall.setx(gameBall.xcor() + gameBall.dx)
    gameBall.sety(gameBall.ycor() + gameBall.dy)


    #Border Bounce
    if gameBall.ycor() > 290:
        gameBall.sety(290)
        gameBall.dy *= -1

    if gameBall.ycor() < -290:
        gameBall.sety(-290)
        gameBall.dy *= -1

   
    if gameBall.xcor() < -390:
        gameBall.goto(0,0)
        gameBall.dx *=-1
        scoreB+=1
        scorePen.clear()
        scorePen.write("Player A : {}     Player B : {}".format(scoreA,scoreB), align= "center",font=("Arial",20,"bold"))


    if gameBall.xcor() > 390:
        gameBall.goto(0,0)
        gameBall.dx *=-1
        scoreA +=1
        scorePen.clear()
        scorePen.write("Player A : {}     Player B : {}".format(scoreA,scoreB), align= "center",font=("Arial",20,"bold"))
    
    
    #Player and Ball collide
   
    if (gameBall.xcor() > 340 and gameBall.xcor() < 350) and (gameBall.ycor() < playerB.ycor() + 40 and gameBall.ycor() > playerB.ycor() - 40 ):
        gameBall.dx *=-1

    if (gameBall.xcor() < -340 and gameBall.xcor() > -350) and (gameBall.ycor() < playerA.ycor() + 40 and gameBall.ycor() > playerA.ycor() - 40 ):
        gameBall.dx *=-1