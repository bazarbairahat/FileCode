import tkinter as tk
import time
import random
class RobotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Робот")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.robot = self.canvas.create_rectangle(180, 180, 220, 220, fill="green")
        self.x, self.y = 200, 200

        self.move_button = tk.Button(root, text="Двигать", command=self.move_robot)
        self.move_button.pack()

    def move_robot(self):
        self.canvas.move(self.robot, 20, 0)  # Двигаем робота на 20 пикселей вправо
        self.x += 20
        self.y += 0

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotGUI(root)
    root.mainloop()
