import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    if name and email and age:
        messagebox.showinfo("Registration Successful", "Name: {}\nEmail: {}\nAge: {}".format(name, email, age))
    else:
        messagebox.showerror("Error", "Please fill in all fields")

root = tk.Tk()
root.title("Registration Form")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

button_register = tk.Button(root, text="Register", command=register)
button_register.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
