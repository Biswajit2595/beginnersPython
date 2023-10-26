import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (q to quit): ").lower()
        if user_choice in ("rock", "paper", "scissors", "q"):
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors (q to quit).")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    draws = 0

    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == "q":
            break
        
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            print("It's a draw!")
            draws += 1
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"User Score: {user_score}, Computer Score: {computer_score}, Draws: {draws}\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()


