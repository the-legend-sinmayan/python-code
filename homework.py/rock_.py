import tkinter as tk
import random

moves = ["Rock", "Paper", "Scissors"]

# Counters for denomination-style tracking
wins = 0
losses = 0
ties = 0

def play(user_choice):
    global wins, losses, ties
    program_choice = random.choice(moves)

    player_label.config(text=f"Player: {user_choice}")
    program_label.config(text=f"Program: {program_choice}")

    if user_choice == program_choice:
        result = "It's a Tie!"
        ties += 1
    elif (user_choice == "Rock" and program_choice == "Scissors") or \
         (user_choice == "Paper" and program_choice == "Rock") or \
         (user_choice == "Scissors" and program_choice == "Paper"):
        result = "You Win!"
        wins += 1
    else:
        result = "Program Wins!"
        losses += 1

    result_label.config(text=result)
    update_counts()

def update_counts():
    win_label.config(text=f"Wins: {wins}")
    loss_label.config(text=f"Losses: {losses}")
    tie_label.config(text=f"Ties: {ties}")

def reset_game():
    global wins, losses, ties
    wins, losses, ties = 0, 0, 0
    player_label.config(text="Player: ")
    program_label.config(text="Program: ")
    result_label.config(text="Result: ")
    update_counts()

# Tkinter window setup
root = tk.Tk()
root.title("Rock Paper Scissors - Denomination Counter")

player_label = tk.Label(root, text="Player: ", font=("Arial", 12))
program_label = tk.Label(root, text="Program: ", font=("Arial", 12))
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))

player_label.pack()
program_label.pack()
result_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=5, pady=5)
paper_button.grid(row=0, column=1, padx=5, pady=5)
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Denomination-style counters
win_label = tk.Label(root, text="Wins: 0", font=("Arial", 12))
loss_label = tk.Label(root, text="Losses: 0", font=("Arial", 12))
tie_label = tk.Label(root, text="Ties: 0", font=("Arial", 12))

win_label.pack()
loss_label.pack()
tie_label.pack()

reset_button = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
