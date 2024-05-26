import tkinter as tk
import random

class DiceRoller(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Генератор случайных чисел")
        self.geometry("400x500")
        self.resizable(False, False)

        self.create_widgets()
        self.dice_animation_running = False

    def create_widgets(self):
        # Диапазон генерации случайного числа
        self.min_label = tk.Label(self, text="Минимальное значение:")
        self.min_label.pack(pady=5)

        self.min_entry = tk.Entry(self)
        self.min_entry.pack(pady=5)

        self.max_label = tk.Label(self, text="Максимальное значение:")
        self.max_label.pack(pady=5)

        self.max_entry = tk.Entry(self)
        self.max_entry.pack(pady=5)

        self.generate_button = tk.Button(self, text="Сгенерировать", height=2, font=("Arial", 12), command=self.generate_random)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="Случайное число:")
        self.result_label.pack(pady=5)

        # Блок для отображения кубиков
        self.dice_frame = tk.Frame(self)
        self.dice_frame.pack(pady=10)

        self.dice1_canvas = tk.Canvas(self.dice_frame, width=100, height=100, bg='white')
        self.dice1_canvas.grid(row=0, column=0, padx=10)

        self.dice2_canvas = tk.Canvas(self.dice_frame, width=100, height=100, bg='white')
        self.dice2_canvas.grid(row=0, column=1, padx=10)

        self.roll_dice_button = tk.Button(self, text="Бросить кубики", height=2, font=("Arial", 12), command=self.start_dice_animation)
        self.roll_dice_button.pack(pady=10)

        self.dice1_value = 1
        self.dice2_value = 1
        self.update_dice(self.dice1_canvas, self.dice1_value)
        self.update_dice(self.dice2_canvas, self.dice2_value)

    def generate_random(self):
        try:
            min_value = int(self.min_entry.get())
            max_value = int(self.max_entry.get())
            if min_value > max_value:
                self.result_label.config(text="Ошибка: мин > макс")
                return
            random_number = random.randint(min_value, max_value)
            self.result_label.config(text=f"Случайное число: {random_number}")
        except ValueError:
            self.result_label.config(text="Ошибка: введите числа")

    def start_dice_animation(self):
        if not self.dice_animation_running:
            self.dice_animation_running = True
            self.dice_animation_steps = 10
            self.animate_dice()

    def animate_dice(self):
        if self.dice_animation_steps > 0:
            self.dice1_value = random.randint(1, 6)
            self.dice2_value = random.randint(1, 6)
            self.update_dice(self.dice1_canvas, self.dice1_value)
            self.update_dice(self.dice2_canvas, self.dice2_value)
            self.dice_animation_steps -= 1
            self.after(100, self.animate_dice)
        else:
            self.dice_animation_running = False

    def update_dice(self, canvas, value):
        canvas.delete("all")
        dot_positions = {
            1: [(50, 50)],
            2: [(30, 30), (70, 70)],
            3: [(30, 30), (50, 50), (70, 70)],
            4: [(30, 30), (70, 30), (30, 70), (70, 70)],
            5: [(30, 30), (70, 30), (50, 50), (30, 70), (70, 70)],
            6: [(30, 30), (70, 30), (30, 50), (70, 50), (30, 70), (70, 70)]
        }
        for pos in dot_positions[value]:
            canvas.create_oval(pos[0] - 5, pos[1] - 5, pos[0] + 5, pos[1] + 5, fill='black')

if __name__ == "__main__":
    app = DiceRoller()
    app.mainloop()
