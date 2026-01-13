import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


def save_and_exit():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    root.destroy() 


root = tk.Tk()
root.title("To-Do List")

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

listbox_tasks = tk.Listbox(root, height=10, width=40)
listbox_tasks.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", width=15, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=15, command=delete_task)
button_delete_task.pack(pady=5)

load_tasks()

button_save_tasks = tk.Button(root, text="Save and Exit", width=15, command=save_and_exit)
button_save_tasks.pack(pady=10)

root.mainloop()
