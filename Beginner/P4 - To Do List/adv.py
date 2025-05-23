import tkinter as tk
from tkinter import messagebox
import os
import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor() 
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, status TEXT DEFAULT 'Pending')""")
conn.commit()


#Load funtion
def fetch_task():
    cursor.execute("SELECT id,task,status FROM tasks")
    return cursor.fetchall()



#Add task function
def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES(?)",(task,))
        conn.commit()
        entry.delete(0,tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning","Please enter a task. ")

#Delete task function
def delete_task():
    selected = listbox.curselection()
    if selected:
        try:
            task_str = listbox.get(selected[0])
            task_id = int(task_str.split(".")[0])
            cursor.execute("DELETE FROM TASKS WHERE ID=?",(task_id,))
            conn.commit()
            update_listbox()
        except Exception as e:
            messagebox.showerror("Error",str(e))
    else:
        messagebox.showwarning("Warning","Please select a task to delete. ")


#Mark tesk as completed
def mark_done():
    selected = listbox.curselection()
    if selected:
        try:
            task_str = listbox.get(selected[0])
            task_id = int(task_str.split(".")[0])
            cursor.execute("UPDATE TASKS SET STATUS='Done' WHERE ID=?",(task_id,))
            conn.commit()
            update_listbox()
        except Exception as e:
            messagebox.showerror("Error",str(e))
        
        
    else:
        messagebox.showwarning("Warning","Please select a task to mark as completed.")

#Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        update_listbox()
     


#Update task function
def update_listbox():
    listbox.delete(0,tk.END)
    for task in fetch_task():
        taks_id, task_text, status = task
        display_text = f"{taks_id}, {task_text},[{status}]"
        listbox.insert(tk.END, display_text)

#GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")


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
del_btn = tk.Button(btn_frame, text="Mark as Done",width=15, command=mark_done, bg="blue", fg="white")
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
fetch_task()

#Run the GUI app
root.mainloop()

conn.close()