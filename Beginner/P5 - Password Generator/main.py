import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        use_digit = digits_var.get()
        use_special = special_var.get()

        if length<4:
            messagebox.showwarning("Warning","Password lenght should be at least 4")
            return 
        
        characters = string.ascii_letters
        if use_digit:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length)) 
        password_entry.delete(0,tk.END)
        password_entry.insert(0,password)
        

    except ValueError:
        messagebox.showerror("Error","Please enter a valid number for password length")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied","Password copied to clipboard!")

# GUI Setup

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False,False)

#Heading
tk.Label(root, text="Generate a Secure Password",font = ("Arial",14,"bold")).pack(pady=10)

# Password Length Input
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Password Length:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
length_entry = tk.Entry(frame, width=5, font=("Arial", 12))
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1)

# Checkboxes
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var, font=("Arial", 11)).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 11)).pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

# Output Entry
password_entry = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
password_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white", font=("Arial", 11)).pack(pady=5)

# Run the app
root.mainloop()