import tkinter as tk
from tkinter import simpledialog, messagebox
from task_manager import TaskManager

tm = TaskManager()  # No constructor needed

def refresh_list():
    listbox.delete(0, tk.END)
    for task in tm.get_tasks():
        listbox.insert(tk.END, f"{task[0]}. {task[1]}")

def add_task_gui():
    title = simpledialog.askstring("Add Task", "Enter task title:")
    if title:
        tm.add_task(title)
        refresh_list()

def update_task_gui():
    selection = listbox.curselection()
    if selection:
        task_text = listbox.get(selection[0])
        task_id = int(task_text.split(".")[0])
        new_title = simpledialog.askstring("Update Task", "Enter new title:")
        if new_title:
            tm.update_task(task_id, new_title)
            refresh_list()
    else:
        messagebox.showwarning("Update Task", "Select a task first!")

def delete_task_gui():
    selection = listbox.curselection()
    if selection:
        task_text = listbox.get(selection[0])
        task_id = int(task_text.split(".")[0])
        tm.delete_task(task_id)
        refresh_list()
    else:
        messagebox.showwarning("Delete Task", "Select a task first!")

# Tkinter GUI
root = tk.Tk()
root.title("To-Do Manager")

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", command=add_task_gui, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update Task", command=update_task_gui, width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task_gui, width=15).grid(row=0, column=2, padx=5)

refresh_list()
root.mainloop()
