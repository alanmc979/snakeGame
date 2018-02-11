from Tkinter import *
class Food:
    def __init__(self):
        self.position = [0,1]
    def generate(self):
        pass

class Snake:

    def __init__(self):
        self.body = [[0, 0], [0, 1]]
        self.size = 10
        self.tail=NONE
        self.head=NONE
        self.direction = "Right"

    def move(self):
        # del self.body[0]
        # self.body.append([self.body[-1][0]+1,self.body[-1][-1]])
        (x, y) = self.body[-1]
        if self.direction== "Right":
            self.body += [[x+1,y]]
        elif self.direction== "Left":
            self.body += [[x - 1, y]]
        elif self.direction == "Up":
            self.body += [[x, y-1]]
        elif self.direction == "Down":
            self.body += [[x,y+1]]
        self.head= self.body[-1]
        self.tail= self.body[0]
        del self.body[0]
    def turn(self, d):
        # self.direction=d
        if d == "Right" and self.direction != "Left":
            self.direction =d
        elif d == "Left" and self.direction != "Right":
            self.direction = d
        elif d == "Up" and self.direction != "Down":
            self.direction= d
        elif d == "Down" and self.direction != "Up":
            self.direction= d

    def grow(self):
        self.body.insert(0, self.tail)

    def render(self, canvas, size):
        for(x,y) in self.body:
            canvas.create_oval(x*size,y*size, (x+1)*size,(y+1)*size, fill="#00FFFF")



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
        # self.size=20
        self.canvas = Canvas(self.frame, width = self.width, height = self.height)
        self.canvas.pack()
        self.frame.bind("<KeyPress>", self.keyboard_even_hanlder)
        # Game entities:
        # self.ball = Ball()
        self.snake= Snake()

    def keyboard_even_hanlder(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.snake.turn(event.keysym)
        elif (event.keysym.lower())==("g"):
            self.snake.grow()

    # Main loop and data/ graphic layer
    def gameLoop(self):
        self.update()   # This is the data layer
        self.render()   # This is the graphic layer
        self.frame.after(100, self.gameLoop)

    def update(self):
        self.snake.move()

    def render(self):
        self.canvas.delete(ALL)
        self.snake.render(self.canvas, 20)
    # Check game stats
    def isOver(self):
        if snake.self.head[0]== self.width or snake.self.head[-1]== self.height
            return True
        for(x,y) in self.body:
            for (a, b) in self.body:
                if (a,b)==(x,y):
                    return True
        return False
g = SnakeGame()
g.gameLoop()
g.frame.mainloop()
