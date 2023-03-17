from turtle import Turtle

class Corpo_Turtle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(position)


    def subir(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def decida(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class bola(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.up()
        self.cord_x = 10
        self.cord_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.cord_x
        new_y = self.ycor() + self.cord_y
        self.goto(new_x, new_y)

    def colision(self):
        self.cord_y *= -1
        self.move_speed *= 0.9

    def colision2(self):
        self.cord_x *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.colision2()
        self.move_speed = 0.1

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.x_score = -1
        self.y_score = -1
        self.hideturtle()
        self.escrever_x()
        self.escrever_y()
    def escrever_x(self):
        self.clear()
        self.x_score += 1
        self.write(f"{self.x_score}  I {self.y_score}", move=False, align='center', font=('Arial', 40, 'normal'))

    def escrever_y(self):
        self.clear()
        self.y_score += 1
        self.write(f"{self.y_score} I {self.x_score}", move=False, align='center', font=('Arial', 40, 'normal'))


