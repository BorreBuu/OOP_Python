import random

choices = ["rock", "paper", "scissors"]
print(random.choice(choices))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif(user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"