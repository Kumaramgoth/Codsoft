import random

choices = ['rock', 'paper', 'scissors']
quit
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    while True:
        
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()

        if player_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break

        if player_choice not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)
        print("-" * 30)

if __name__ == "__main__":
    play_game()