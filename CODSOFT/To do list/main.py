import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

#main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="black")
task_entry = tk.Entry(root, width=40, bg="white")
task_entry.pack(pady=20, ipady=15)
root.geometry("400x400")


#add task button
add_task_button = tk.Button(root, text="Add Task", width=32, bg="green", command=add_task)
add_task_button.pack(pady=10)

#tasks listbox
tasks_listbox = tk.Listbox(root, width=40, height=10)
tasks_listbox.pack(pady=10, ipady=10)

#delete task button
delete_task_button = tk.Button(root, text="Delete Task", width=32,bg="red", command=delete_task)
delete_task_button.pack(pady=5)


root.mainloop()
