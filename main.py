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

    if head.distance(eat)<20:
        x= random.randint(-280,280)
        y= random.randint(-280,280)
        eat.goto(x,y)
    
    

    move()
    time.sleep(posponer)