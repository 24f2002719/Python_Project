import tkinter as tk
from tkinter import messagebox
import os

tasks = []

#Load funtion
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("P4 - To Do List/tasks.txt","r") as file:
            for line in file:
                tasks.append(line.strip())
                update_listbox()


#Save tasks
def save_tasks():
    with open("P4 - To Do List/tasks.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")


#Add task function
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0,tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning","Please enter a task. ")

#Delete task function
def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning","Please select a task to delete. ")


#Mark tesk as completed
def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if not task.endswith(" [Done]"):
            tasks[index]= task + " [Done]"
            update_listbox()
            save_tasks()
        else:
            messagebox.showinfo("Info","Taks already marked as done. ")
    else:
        messagebox.showwarning("Warning","Please select a task to mark as completed.")

#Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()
        save_tasks()


#Update task function
def update_listbox():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)


#GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False,False)

#Title
label = tk.Label(root, text="My To-Do list", font=("Arial",16))
label.pack(pady=10)

#Input box
entry = tk.Entry(root, font=("Arial",14), width=40)
entry.pack(pady=5)

#Buttons
btn_frame=tk.Frame(root)
btn_frame.pack(pady=10)

#Add Button
add_btn = tk.Button(btn_frame, text = "Add Task",command=add_task, font=("Arial",12), bg = "green",fg="white")
add_btn.grid(row=0,column=0,padx=5)


#Delete button
del_btn = tk.Button(btn_frame, text="Mark as Done",width=15, command=mark_completed, bg="blue", fg="white")
del_btn.grid(row=1,column=0,padx=5,pady=5)

#Done button
done_btn = tk.Button(btn_frame, text="Delete Selected Task", command=delete_task, font=("Arial",12),bg="red", fg="white")
done_btn.grid(row=0,column=1,padx=5)


#Clear button
clear_btn = tk.Button(btn_frame, text="Clear all",width=15, command=clear_tasks, bg="gray", fg="white")
clear_btn.grid(row=1,column=1,padx=5,pady=5)




#ListBox
listbox = tk.Listbox(root, font=("Arial",12), width=50, height=15)
listbox.pack(pady=10)

#Load tasks when app starts
load_tasks()

#Run the GUI app
root.mainloop()