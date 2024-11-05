import tkinter as tk
import json
from tkinter import messagebox

def save_data():
    student_name = name_entry.get()
    missed_classes = missed_entry.get()
    
    # Перевірка на заповненість полів
    if not student_name or not missed_classes:
        messagebox.showerror("Помилка", "Заповніть усі поля")
        return
    
    try:
        missed_classes = int(missed_classes)
    except ValueError:
        messagebox.showerror("Помилка", "Кількість пропущених занять має бути числом")
        return

    data = {
        "student_name": student_name,
        "missed_classes": missed_classes
    }

    try:
        with open("students_data.json", "a") as file:
            json.dump(data, file)
            file.write("\n")
        messagebox.showinfo("Успіх", "Дані збережено успішно")
        name_entry.delete(0, tk.END)
        missed_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти дані: {e}")

root = tk.Tk()
root.title("Журнал пропусків студентів")
root.geometry("480x350")
root.configure(bg="grey")

name_label = tk.Label(root, text="Ім'я студента:", bg="grey")
name_label.place(x=50, y=50)
name_entry = tk.Entry(root)
name_entry.place(x=200, y=50)

missed_label = tk.Label(root, text="Кількість пропущених занять:", bg="grey")
missed_label.place(x=50, y=100)
missed_entry = tk.Entry(root)
missed_entry.place(x=200, y=100)

save_button = tk.Button(root, text="Зберегти", command=save_data)
save_button.place(x=200, y=150)

root.mainloop()
