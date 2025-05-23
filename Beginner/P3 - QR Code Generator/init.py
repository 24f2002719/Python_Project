import qrcode

#first Method
'''

data = input("Enter the data or URL to generate QR Code : ")

qr = qrcode.make(data)

filename = input("Enter filename to save (without extension): ")

qr.save(f"assest/{filename}.png")

print(f"QR code generated and saved as {filename}.png")'''


#second method
'''
data = input("Enter the data or URL to generate QR Code : ")

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(data)
qr.make(fit=True)

#Customizing the QR Code

fill_color = input("Enter the color for the QR code (e.g. black, blue, red etc,)")
back_color = input("Enter the background color for the QR code (e.g. black, blue, red etc,)")

img = qr.make_image(fill_color=fill_color,back_color=back_color)

filename = input("Enter filename to save (without extension): ")

img.save(f"assest/{filename}.png")

print(f"QR code generated and saved as {filename}.png")'''


# Third Method

import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr():
    data = entry.get()
    if data == "":
        messagebox.showerror("Error","Please enter some data to generate QR Code")
        return
    qr = qrcode.QRCode(version=1,box_size=10,border=5)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color = "white")

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
filetypes=[("PNG files","*.png")])
    if file_path:
        img.save(file_path)

    messagebox.showinfo("Success", f"QR Code saved at {file_path}")

#setting up the GUI window
root  = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")
root.resizable(False, False)

#Heading
label = tk.Label(root, text= "Enter Data for QR Code", font=("Arial",14))
label.pack(pady=10)

#Text entry
entry = tk.Entry(root, width=40, font=("Arial,12"))
entry.pack(pady=5)

#Button
button = tk.Button(root,text="Generate QR Code", command=generate_qr, font=("Arial",12),bg="blue", fg="white")
button.pack(pady=20)

root.mainloop()


