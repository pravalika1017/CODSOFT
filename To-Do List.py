

from tkinter import *
from tkinter import messagebox
import os

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("Smart To-Do List")
root.geometry("500x650")
root.config(bg="#0f172a")
root.resizable(False, False)

# ---------------- FUNCTIONS ----------------

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, "📝 " + task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")


def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if "✔" not in task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, "✔ DONE - " + task)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")


def clear_tasks():
    confirm = messagebox.askyesno("Clear", "Delete all tasks?")

    if confirm:
        task_listbox.delete(0, END)
        save_tasks()


def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())


# ---------------- TITLE ----------------

title = Label(
    root,
    text="✨ TO-DO LIST ✨",
    font=("Poppins", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=20)

# ---------------- INPUT FRAME ----------------

input_frame = Frame(root, bg="#0f172a")
input_frame.pack(pady=10)

task_entry = Entry(
    input_frame,
    font=("Arial", 16),
    width=22,
    bd=0,
    bg="#e2e8f0",
    fg="#000000"
)
task_entry.grid(row=0, column=0, padx=10, ipady=10)

add_btn = Button(
    input_frame,
    text="ADD",
    font=("Arial", 12, "bold"),
    bg="#22c55e",
    fg="white",
    padx=15,
    pady=10,
    bd=0,
    command=add_task
)
add_btn.grid(row=0, column=1)

# ---------------- TASK LIST ----------------

frame = Frame(root, bg="#0f172a")
frame.pack(pady=20)

scrollbar = Scrollbar(frame)

task_listbox = Listbox(
    frame,
    font=("Arial", 14),
    width=38,
    height=15,
    bg="#1e293b",
    fg="white",
    selectbackground="#38bdf8",
    activestyle="none",
    bd=0,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.pack()

# ---------------- BUTTONS ----------------

button_frame = Frame(root, bg="#0f172a")
button_frame.pack(pady=20)

done_btn = Button(
    button_frame,
    text="✔ DONE",
    font=("Arial", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    padx=15,
    pady=10,
    bd=0,
    command=mark_done
)
done_btn.grid(row=0, column=0, padx=10)

delete_btn = Button(
    button_frame,
    text="🗑 DELETE",
    font=("Arial", 11, "bold"),
    bg="#ef4444",
    fg="white",
    padx=15,
    pady=10,
    bd=0,
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=10)

clear_btn = Button(
    button_frame,
    text="CLEAR ALL",
    font=("Arial", 11, "bold"),
    bg="#f59e0b",
    fg="white",
    padx=15,
    pady=10,
    bd=0,
    command=clear_tasks
)
clear_btn.grid(row=0, column=2, padx=10)

# ---------------- FOOTER ----------------

footer = Label(
    root,
    text="Developed using Python Tkinter",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#94a3b8"
)
footer.pack(side=BOTTOM, pady=10)

# ---------------- LOAD SAVED TASKS ----------------

load_tasks()

# ---------------- RUN APP ----------------

root.mainloop()
