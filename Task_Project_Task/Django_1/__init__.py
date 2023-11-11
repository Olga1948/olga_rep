from tkinter import *
from random import randint


class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[14, 14]]
        self.food_coords = [randint(0, 29) for i in range(2)]
        self.vector = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.GAME()


    def set_food(self): # для каждого последующего положения еды
        self.food_coords = [randint(0, 29) for i in range(2)]
        if self.food_coords in self.snake_coords: # условие, чтобы еда не лежала на змейке
            self.set_food()


    def set_direction(self, event):# для нового направления змейки
        if event.keysym in self.vector:# для проверки нажатия кнопки
            self.direction = self.vector[event.keysym]

    def draw(self): # облик игры
        self.canvas.delete(ALL)
        x_food, y_food = self.food_coords
        self.canvas.create_rectangle(x_food *10, y_food *10, (x_food +1) *10, (y_food +1) *10, fill="red", width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="green", width=0)

    @staticmethod # для возрата координаты на интервале [0, 29]
    def coord_check(coord):
        return 0 if coord > 29 else 29 if coord < 0 else coord

    # Алгоритм "Оторванный Хвост\Логика игры"
    def GAME(self):
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0];
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.food_coords[0] and y == self.food_coords[1]:
            self.set_food()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.GAME)

root = Tk()# Каркас игры
canvas = Canvas(root, width=400, height=400, bg="black")
canvas.pack()
game = Game(canvas)
root.mainloop()
