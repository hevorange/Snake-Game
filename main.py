import turtle
import time

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
    move()
    time.sleep(posponer)