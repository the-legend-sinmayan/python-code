import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def create_gui():
    root = tk.Tk()
    root.title("Random Password Generator")

 
    label = tk.Label(root, text="Click Generate to create a password", font=("Arial", 12))
    label.pack(pady=10)

   
    password_entry = tk.Entry(root, width=30, font=("Arial", 14))
    password_entry.pack(pady=10)

  
    def on_generate():
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generate_password())

    generate_button = tk.Button(root, text="Generate", command=on_generate,
                                font=("Arial", 12), bg="blue", fg="white")
    generate_button.pack(pady=10)

    root.mainloop()


create_gui()
