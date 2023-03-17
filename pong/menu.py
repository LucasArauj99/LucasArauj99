from classes import Corpo_Turtle, bola, Placar
from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("poing")
screen.tracer(0)

tart_x = Corpo_Turtle((350, 0))
tart_y = Corpo_Turtle((-350, 0))
bol = bola()
placar = Placar()

screen.listen()
screen.onkey(tart_x.subir, "Up")
screen.onkey(tart_x.decida, "Down")
screen.onkey(tart_y.subir, "w")
screen.onkey(tart_y.decida, "s")

end_game = True
while end_game:
    time.sleep(bol.move_speed)
    screen.update()
    bol.move()

    if bol.ycor() > 270 or bol.ycor() < -270:
        bol.colision()

    if bol.distance(tart_x) < 50 and bol.xcor() > 320 or bol.distance(tart_y) < 50 and bol.xcor() < -320:
        bol.colision2()

    if bol.xcor() > 360:
        bol.reset_pos()
        placar.escrever_x()

    if bol.xcor() < -360:
        bol.reset_pos()
        placar.escrever_y()
        

screen.exitonclick()






