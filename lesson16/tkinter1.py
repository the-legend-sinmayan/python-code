from tkinter import *
window = Tk()
window.title("tkinter sample window")
window.geometry("300x300")


greeting = Label(text = "Hello, User!", fg ='black' , bg = 'white')
button  = Button(text = "click me", bg =  'black',fg = 'white')
entry = Entry(fg= 'yellow', bg = 'blue', width = 50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label  =label = Label(master=frame, text="simple frame")
label.pack()

textbox = Text(fg = 'green', bg ='blue')
textbox.pack()