import tkinter as tk
import random

# Функция для перемещения фигуры
def move_figure(figure):
    global figures
    x, y, width, height, dx, dy = figures[figure]  # Получаем данные о фигуре
    canvas.move(figure, dx, dy)  # Перемещаем фигуру на dx и dy пикселей

    # Проверяем, чтобы фигура не вышла за пределы окна
    if x + dx < 0 or x + width + dx > canvas_width:
        dx = -dx  # Изменяем направление движения по x
    if y + dy < 0 or y + height + dy > canvas_height:
        dy = -dy  # Изменяем направление движения по y

    # Обновляем данные о фигуре
    figures[figure] = (x + dx, y + dy, width, height, dx, dy)

    # Запускаем функцию снова через 10 миллисекунд
    canvas.after(10, lambda: move_figure(figure))

# Создаем главное окно
root = tk.Tk()
root.title("Анимация фигур")

# Создаем Canvas (холст) для отображения анимации
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightgray")  # Устанавливаем фон холста
canvas.pack()

# Создаем список фигур и их параметров: (x, y, width, height, dx, dy)
figures = {}

# Создаем шарики
for _ in range(3):
    x = random.randint(0, canvas_width - 20)  # Случайное начальное положение по x
    y = random.randint(0, canvas_height - 20)  # Случайное начальное положение по y
    width = 20
    height = 20
    dx = random.choice([-2, 2])  # Случайное начальное направление по x
    dy = random.choice([-2, 2])  # Случайное начальное направление по y
    color = random.choice(['red', 'green', 'blue', 'orange', 'purple'])  # Случайный цвет
    figure = canvas.create_oval(x, y, x + width, y + height, fill=color, outline="white", width=2)  # Устанавливаем белый внутренний бордер
    figures[figure] = (x, y, width, height, dx, dy)
    move_figure(figure)

# Создаем кубы
for _ in range(3):
    x = random.randint(0, canvas_width - 20)  # Случайное начальное положение по x
    y = random.randint(0, canvas_height - 20)  # Случайное начальное положение по y
    width = 20
    height = 20
    dx = random.choice([-2, 2])  # Случайное начальное направление по x
    dy = random.choice([-2, 2])  # Случайное начальное направление по y
    color = random.choice(['red', 'green', 'blue', 'orange', 'purple'])  # Случайный цвет
    figure = canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="white", width=2)  # Устанавливаем белый внутренний бордер
    figures[figure] = (x, y, width, height, dx, dy)
    move_figure(figure)

# Запускаем главный цикл программы
root.mainloop()
