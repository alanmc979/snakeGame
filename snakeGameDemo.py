from tkinter import *

class Snake:

    def __init__(self):
        self.body = [[0 , 0], [0, 1]]
        self.size = 10

    def move(self):
        pass

    def grow(self):
        pass

    def render(self):
        pass

class Ball:

    # Data layer below
    def __init__(self):
        print ("Ball initialing")
        self.x = 30
        self.y = 30
        self.dx = 0
        self.dy = 0
        self.len = 30

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dx = self.dx * 0.995
        self.dy = self.dy * 0.995

    def accelerate(self, ax, ay):
        self.dx += ax
        self.dy += ay

    # Graphic layer below
    def render(self, canvas):
        assert (isinstance(canvas, Canvas))
        canvas.create_oval(self.x, self.y, self.x + self.len, self.y + self.len)

class SnakeGame:

    # Constructor
    def __init__(self):
        print("Snake initialing")
        self.frame = Tk()
        self.width = 800
        self.height = 600
        self.canvas = Canvas(self.frame, width = self.width, height = self.height)
        self.canvas.pack()
        self.frame.bind("<KeyPress>", self.keyboard_even_hanlder)
        # Game entities:
        self.ball = Ball()

    def keyboard_even_hanlder(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if event.keysym == "Up":
                self.ball.accelerate(0, -0.2)
            elif event.keysym == "Down":
                self.ball.accelerate(0, 0.2)
            elif event.keysym == "Left":
                self.ball.accelerate(-0.2, 0)
            else:
                self.ball.accelerate(0.2, 0)


    def gameLoop(self):
        self.update()   # This is the data layer
        self.render()   # This is the graphic layer
        self.frame.after(20, self.gameLoop)

    def update(self):
        self.ball.move()
        if self.ball.x <= 0:
            self.ball.dx = abs(self.ball.dx)
        if self.ball.x + self.ball.len >= self.width:
            self.ball.dx = - abs(self.ball.dx)

    def render(self):
        self.canvas.delete(ALL)
        self.ball.render(self.canvas)

g = SnakeGame()
g.gameLoop()
g.frame.mainloop()