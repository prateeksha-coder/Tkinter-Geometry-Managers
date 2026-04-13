import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("RPS Game")

choices = ["Rock", "Paper", "Scissors"]

# Main game logic
def play(user_choice):
    computer = random.choice(choices)

    if user_choice == computer:
        result = "Tie"
    elif (user_choice == "Rock" and computer == "Scissors") or \
         (user_choice == "Paper" and computer == "Rock") or \
         (user_choice == "Scissors" and computer == "Paper"):
        result = "You Win"
    else:
        result = "Computer Wins"

    # Update labels
    user_label["text"] = "You: " + user_choice
    comp_label["text"] = "Computer: " + computer
    result_label["text"] = result

# Separate functions (instead of lambda)
def choose_rock():
    play("Rock")

def choose_paper():
    play("Paper")

def choose_scissors():
    play("Scissors")

# Labels
user_label = tk.Label(root, text="You: ")
user_label.pack()

comp_label = tk.Label(root, text="Computer: ")
comp_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Buttons (no lambda)
tk.Button(root, text="Rock", command=choose_rock).pack()
tk.Button(root, text="Paper", command=choose_paper).pack()
tk.Button(root, text="Scissors", command=choose_scissors).pack()

# Run app
root.mainloop()