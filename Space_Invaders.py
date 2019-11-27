import turtle
import winsound
import math
import random
#set up screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SPACE INVADERS")
wn.bgpic("background.gif")
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")

#Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
    border_pen.forward(500)
    border_pen.left(90)
border_pen.hideturtle()

score = 0
#ScoreBoard
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-240,230)
scorestring = "Score: %s" %score
score_pen.write(scorestring,False,align = "left",font=("Arial",12,"normal"))
score_pen.hideturtle()



#Player
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-200)
player.setheading(90)

#Create bullet
bulletspeed = 20

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bullet.hideturtle()


enemy_no = 5
enemies = []
for i in range(enemy_no):
    enemies.append(turtle.Turtle())
    
#create enemy
enemyspeed = 2
for enemy in enemies:
    enemy.color("green")
    enemy.shape("enemy.gif")
    enemy.penup()
    x = random.randint(-200,200)
    y = random.randint(50,200)
    enemy.setposition(x,y)


playerspeed = 15
def fire_bullet():

        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()
        

#Move player
def move_left():
    x = player.xcor()
    x-=playerspeed
    if x<-230:
        x = - 230
    player.setx(x)

def move_right():
    x = player.xcor()
    x+=playerspeed
    if x>230:
        x =  230
    player.setx(x)



def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

    
#create keyboard work
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#MainLoop
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        
        if enemy.xcor() > 230:
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)
            enemyspeed *= -1
            
        if enemy.xcor() < -230:
            for e in enemies:
                y = e.ycor()
                y -= 50
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet,enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            #Reset bullet
            bullet.hideturtle()
            bullet.setposition(0,-350)
            #Reset enemy
            x = random.randint(-200,200)
            y = random.randint(50,200)
            enemy.setposition(x,y)
            score +=10
            score_pen.clear()
            scorestring = "Score: %s" %score
            score_pen.write(scorestring,False,align = "left",font=("Arial",12,"normal"))

     

        flag = 1
        if isCollision(player,enemy):
            winsound.PlaySound("game_over.wav", winsound.SND_ASYNC)
            over_pen = turtle.Turtle()
            over_pen.speed(0)
            over_pen.color("red")
            over_pen.penup()
            over_pen.setposition(5,20)
            overstring = "Game Over"
            over_pen.write(overstring,False,align = "center",font=("Arial",25,"normal"))
            over_pen.hideturtle()
            for e1 in enemies:
                e1.hideturtle()
            player.hideturtle()
            flag = 0
            break

            
    if flag == 0:
        break

    if score==100:
        win_pen = turtle.Turtle()
        win_pen.speed(0)
        win_pen.color("yellow")
        win_pen.penup()
        win_pen.setposition(5,20)
        winstring = "You Won"
        win_pen.write(winstring,False,align = "center",font=("Arial",25,"normal"))
        win_pen.hideturtle()
        for e2 in enemies:
            e2.hideturtle()
        player.hideturtle()
        break


   #Move bullet
    if bullet.isvisible():
       y = bullet.ycor() + bulletspeed
       bullet.sety(y)
    if bullet.ycor() > 225:
        bullet.hideturtle()


    



