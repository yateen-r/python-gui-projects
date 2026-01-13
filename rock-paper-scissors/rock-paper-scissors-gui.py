import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def play_game(user_choice):
    global user_score, computer_score, round_counter

    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    
    result_label.config(text=f"Computer chose: {computer_choice}")

    
    if winner == "user":
        user_score += 1
        messagebox.showinfo("Result", "You win this round!")
    elif winner == "computer":
        computer_score += 1
        messagebox.showinfo("Result", "You lose this round!")
    else:
        messagebox.showinfo("Result", "It's a tie!")

   
    round_counter += 1
    score_label.config(text=f"Round {round_counter} | You: {user_score} - Computer: {computer_score}")


user_score = 0
computer_score = 0
round_counter = 0


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#f0f0f0")  


title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=('Helvetica', 18, 'bold'), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Choose your option:", font=('Helvetica', 12), bg="#f0f0f0", fg="#333")
instruction_label.pack(pady=10)


button_style = {
    'font': ('Helvetica', 12, 'bold'),
    'bg': '#4CAF50',
    'fg': 'white',
    'activebackground': '#45a049',
    'width': 15,
    'height': 2,
    'bd': 0,
}


rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'), **button_style)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'), **button_style)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'), **button_style)
scissors_button.pack(pady=10)


result_label = tk.Label(root, text="", font=('Helvetica', 12), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)


score_label = tk.Label(root, text="Round 0 | You: 0 - Computer: 0", font=('Helvetica', 12, 'bold'), bg="#f0f0f0", fg="#333")
score_label.pack(pady=10)


root.mainloop()
