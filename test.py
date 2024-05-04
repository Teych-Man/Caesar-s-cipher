import tkinter as tk
from tkinter import ttk
import threading
import test3

def simulate_loading():
    test3.simulate_loading2()

root = tk.Tk()
root.title("Прогресс-бар - Загрузка приложения")

progress_frame = ttk.Frame(root)
progress_frame.pack(pady=20)

progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(padx=10, pady=10)

start_button = ttk.Button(root, text="Запустить загрузку", command=simulate_loading)
start_button.pack(pady=10)

root.mainloop()
