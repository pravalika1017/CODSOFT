import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=" * 50)
print("WELCOME TO ROCK-PAPER-SCISSORS GAME")
print("=" * 50)

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice.capitalize())
    print("Computer Choice:", computer_choice.capitalize())

    # Determine winner
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nSCOREBOARD")
    print("-" * 20)
    print("You      :", user_score)
    print("Computer :", computer_score)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFINAL SCORE")
        print("-" * 20)
        print("You      :", user_score)
        print("Computer :", computer_score)

        if user_score > computer_score:
            print("Congratulations! You are the overall winner.")
        elif computer_score > user_score:
            print("Computer is the overall winner.")
        else:
            print("Overall Match Tied.")

        print("\nThank you for playing.")
        break