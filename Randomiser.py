import tkinter as tk
import random
import subprocess
import threading

def generate_random_number(min_value, max_value):
    random_number = random.randint(min_value, max_value)
    return random_number

def open_on_screen_keyboard():
    subprocess.run('osk.exe', shell=True)

def generate_random():
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())

    random_number = generate_random_number(min_value, max_value)

    result_label.config(text=f"Случайное число: {random_number}")

# Открываем экранную клавиатуру в отдельном потоке
keyboard_thread = threading.Thread(target=open_on_screen_keyboard)
keyboard_thread.start()

root = tk.Tk()
root.title("Генератор случайных чисел")
root.geometry("300x200")  # Изменим размер окна на 300x200


# Создание меток, полей ввода и кнопки
min_label = tk.Label(root, text="Минимальное значение:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()

max_label = tk.Label(root, text="Максимальное значение:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()

generate_button = tk.Button(root, text="Сгенерировать", command=generate_random)
generate_button.pack()

result_label = tk.Label(root, text="Случайное число:")
result_label.pack()

root.mainloop()