from tkinter import *

class Apple:

    def __init__(self):
        self.x = 100
        self.y = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Launcher:

    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 800, height = 600, bg = "salmon3")
        self.canvas.pack()
        # Create a apple
        self.apple = Apple()

    def update(self):
        self.canvas.delete(ALL)
        self.canvas.create_oval(self.apple.x, self.apple.y, self.apple.x + 40, self.apple.y + 40)
        self.apple.move(2, 0)
        self.root.after(50, self.update)

launcher = Launcher()
launcher.update()
launcher.root.mainloop()