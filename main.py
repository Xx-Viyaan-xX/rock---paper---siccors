import random

def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def play_game():
    print("welcome to rock, paper and scissors")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
    result=determine_winner(user_choice,computer_choice)
    print(result)

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "its a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissors" and computer_choice == "paper"):
        return "You win"
    else:
        return "computer wins"
    
if __name__== "__main__":
    play_game()