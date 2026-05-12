import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissor"]


def determine_winner(user_choice, program_choice):
    if user_choice == program_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and program_choice == "Scissor") or \
         (user_choice == "Paper" and program_choice == "Rock") or \
         (user_choice == "Scissor" and program_choice == "Paper"):
        return "You Win!"
    else:
        return "Program Wins!"


def play(user_choice):
    program_choice = random.choice(choices)
    user_label.config(text=f"Your Choice: {user_choice}")
    program_label.config(text=f"Program Choice: {program_choice}")
    result_label.config(text=determine_winner(user_choice, program_choice))


def reset_game():
    user_label.config(text="Your Choice: ")
    program_label.config(text="Program Choice: ")
    result_label.config(text="Result: ")


root = tk.Tk()
root.title("Rock Paper Scissor Game")


user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack(pady=5)

program_label = tk.Label(root, text="Program Choice: ", font=("Arial", 12))
program_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissor_button = tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("Scissor"))
scissor_button.grid(row=0, column=2, padx=5)


reset_button = tk.Button(root, text="Reset Game", width=15, command=reset_game, bg="red", fg="white")
reset_button.pack(pady=10)


root.mainloop()
