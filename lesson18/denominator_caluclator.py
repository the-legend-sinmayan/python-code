from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Image


# Welcome Label
label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.askyesno(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox:  # True if Yes
        topwin()

# Button
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white')
button1.place(x=260, y=360)

def topwin():
    # Top Window
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    # Widgets inside Top Window
    Label(top, text="Enter Amount:", bg='grey').place(x=200, y=50)
    entry = Entry(top)
    entry.place(x=300, y=50)

    def calculate():
        try:
            amount = int(entry.get())
            # Example: split into denominations
            hundreds = amount // 100
            fifties = (amount % 100) // 50
            tens = (amount % 50) // 10
            lbl_result.config(text=f"100s: {hundreds}, 50s: {fifties}, 10s: {tens}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculate)
    btn.place(x=260, y=100)

    lbl_result = Label(top, text="", bg='grey')
    lbl_result.place(x=200, y=150)

root.mainloop()
