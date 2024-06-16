import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        
        if winner == 'tie':
            print("It's a tie!")
        elif winner == 'user':
            user_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("You lose!")
        
        print(f"Score - User: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()
