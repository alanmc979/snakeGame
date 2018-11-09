from tkinter import *
from tkinter import font
import random
import pygame
	
class Food:
    # Try to implement this in OOP way
    def __init__(self, width, height):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.color = random.choice(["#FF0080", "#00FFAB", "#00FFAB"])

    def render(self, canvas, size):
        canvas.create_oval(self.x * size, self.y * size, (self.x + 1) * size, (self.y + 1) * size, fill=self.color)

class Snake:

    def __init__(self):
        self.body = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.tail = None
        self.direction = "Right"

    def turn(self, d):
        if d == "Right" and self.direction != "Left":
            self.direction = d
        if d == "Left" and self.direction != "Right":
            self.direction = d
        if d == "Up" and self.direction != "Down":
            self.direction = d
        if d == "Down" and self.direction != "Up":
            self.direction = d

    def move(self):
        (x, y) = self.body[-1]
        if self.direction == "Right":
            self.body += [[x+1, y]]
        elif self.direction == "Left":
            self.body += [[x-1, y]]
        elif self.direction == "Up":
            self.body += [[x, y-1]]
        elif self.direction == "Down":
            self.body += [[x, y+1]]
        self.tail = self.body[0]
        del self.body[0]

    def grow(self):
        self.body.insert(0, self.tail)

    def render(self, canvas, size):
        for (x, y) in self.body:
            canvas.create_oval(x * size, y * size, (x + 1)*size, (y+1)*size, fill="#A200FF")

class SnakeGame:

    class State:
        RUNNING = 0
        GAMEOVER = 1

    # Constructor
    def __init__(self):
        print("Snake initialing")
        self.frame = Tk()
        self.width = 40
        self.height = 30
        self.size = 20
        self.canvas = Canvas(self.frame, width = self.width * self.size, height = self.height * self.size, bg="#222222")
        self.canvas.pack()
        self.frame.bind("<KeyPress>", self.keyboard_even_hanlder)
        # Game entities:
        self.snake = Snake()
        self.food = Food(self.width, self.height)
        # Game Status:
        self.state = self.State.RUNNING
        # Game Effects:
        pygame.mixer.init()
        self.sound_eat = pygame.mixer.Sound("./eat.wav")
        self.sound_over = pygame.mixer.Sound("./over.wav")

    def keyboard_even_hanlder(self, event):
        if self.state == self.State.RUNNING:
            if event.keysym in ["Up", "Down", "Left", "Right"]:
                self.snake.turn(event.keysym)

        if self.state == self.State.GAMEOVER:
            if event.keysym == 'Return':
                self.snake = Snake()
                self.food = Food(self.width, self.height)
                self.state = self.State.RUNNING



    # Main loop and data / graphic layer
    def gameLoop(self):
        self.update()   # This is the data layer
        self.render()   # This is the graphic layer
        self.frame.after(100, self.gameLoop)

    def update(self):
        if self.state == self.State.RUNNING:
            self.snake.move()
            # Check if you eat the food.
            if self.snake.body[-1] == [self.food.x, self.food.y]:
                self.sound_eat.play()
                self.snake.grow()
                del self.food
                self.food = Food(self.width, self.height)

            if self.isOver():
                self.sound_over.play()
                del self.food
                del self.snake
                self.state = self.State.GAMEOVER


    def render(self):
        if self.state == self.State.RUNNING:
            self.canvas.delete(ALL)
            self.snake.render(self.canvas, self.size)
            self.food.render(self.canvas, self.size)

        if self.state == self.State.GAMEOVER:
            self.canvas.delete(ALL)
            self.canvas.create_text(400, 300, text="Game Over", fill="#FF0080", font=font.Font(size=36, weight='bold'))

    # For checking game status
    def isOver(self):
        head = self.snake.body[-1]
        # Check boundary
        if head[0] > self.width or head[0] < 0:
            return True
        if head[1] > self.height or head[1] < 0:
            return True
        # Check eat body
        if head in self.snake.body[:-1]:
            return True


g = SnakeGame()
g.gameLoop()
g.frame.mainloop()
