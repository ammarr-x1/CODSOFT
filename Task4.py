import random

def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()

    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "YOU WIN!"

    else:
        return "COMPUTER WINS!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    comp_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\tYOU | COMP")
        print("\t ",user_score,"| ",comp_score)
        print("Your choice ", user_choice)
        print("Computer choice ",computer_choice)

        result = winner(user_choice, computer_choice)

        if result.strip().lower() == "you win!":
            print(result)
            user_score += 1

        else:
            print(result)
            comp_score += 1
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
