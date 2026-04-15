import turtle

turtle.Screen().bgcolor("lightblue")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("welcome to turtle window")

board = turtle.Turtle()

for i in range(4):
    board.forward(1000)
    board.left(900)
    i = i+1