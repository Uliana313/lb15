import tkinter as tk
from tkinter import messagebox 

def save_settings():
    width = width_entry.get()
    height = height_entry.get()
    color = color_entry.get()
    
    if not width or not height or not color:
        messagebox.showerror("Помилка", "Заповніть усі поля")
        return
    
    settings = f"Width: {width}\nHeight: {height}\nColor: {color}\n"
    
    with open("settings.txt", "w") as file:
        file.write(settings)
    
    messagebox.showinfo("Успіх", "Налаштування збережено успішно")

root = tk.Tk()
root.title("Налаштування вікна")

frame = tk.Frame(root, bg="lightgrey", width=300, height=200)
frame.pack_propagate(False) 
frame.pack(padx=10, pady=10)

width_label = tk.Label(frame, text="Ширина:")
width_label.pack()
width_entry = tk.Entry(frame)
width_entry.pack()

height_label = tk.Label(frame, text="Висота:")
height_label.pack()
height_entry = tk.Entry(frame)
height_entry.pack()

color_label = tk.Label(frame, text="Колір:")
color_label.pack()
color_entry = tk.Entry(frame)
color_entry.pack()

save_button = tk.Button(frame, text="Зберегти налаштування", command=save_settings)
save_button.pack(pady=10)

root.mainloop()

