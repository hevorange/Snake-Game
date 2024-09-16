import turtle
import time
import random

posponer = 0.1

#Creamos la ventana del juego
screen = turtle.Screen()
#asignamos atributos a la ventana
screen.title('Snake - Game ')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

#Crear la cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'

#comida
eat = turtle.Turtle()
eat.speed(0)
eat.shape('circle')
eat.color('red')
eat.penup()
eat.goto(0,100)

#Cuerpo de la serpiente

bodySnake=[] 


#functions 
def UpHead():
    head.direction='up'

def DownHead():
    head.direction='down'

def LeftHead():
    head.direction='left'

def RightHead():
    head.direction='right'


def move ():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    
    elif head.direction == 'down':
        y= head.ycor()
        head.sety(y-20)

    elif head.direction == 'left':
        x= head.xcor()
        head.setx(x-20)

    elif head.direction == 'right':
        x= head.xcor()
        head.setx(x+20)

#Keyboard
screen.listen()
screen.onkeypress(UpHead,'Up')
screen.onkeypress(DownHead,'Down')
screen.onkeypress(LeftHead,'Left')
screen.onkeypress(RightHead,'Right')

while True:
    screen.update()

    #coliciones con los bordes
    if head.xcor()>280 or head.xcor() < -280 or head.ycor()>280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        for index in bodySnake:
            index.goto(1000,1000)
        
        bodySnake.clear()

    if head.distance(eat)<20:
        x= random.randint(-280,280)
        y= random.randint(-280,280)
        eat.goto(x,y)

        bodyPart = turtle.Turtle()
        bodyPart.speed(0)
        bodyPart.shape('square')
        bodyPart.color('grey')
        bodyPart.penup()
        bodySnake.append(bodyPart)

    # Mover cuerpo de la serpiente
    TotalBody= len(bodySnake)
    for index in range(TotalBody-1,0,-1):
        x = bodySnake[index-1].xcor()
        y = bodySnake[index-1].ycor()
        bodySnake[index].goto(x,y)
    
    if TotalBody >0:
        x=head.xcor()
        y=head.ycor()
        bodySnake[0].goto(x,y)
    
    

    move()

    #coliciones con el cuerpo de la serpiente
    for index in bodySnake:
        if index.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            for bodypart in bodySnake:
                bodypart.goto(1000,1000)
            bodySnake.clear()
                

    time.sleep(posponer)