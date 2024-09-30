import random
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    
    return "Computer wins!"
def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        
        player_input = input("Enter your choice (1/2/3) or 4 to exit: ")
        
        if player_input == '4':
            print("Thanks for playing! Goodbye!")
            break

        if player_input not in ['1', '2', '3']:
            print("Invalid choice, please try again.")
            continue
        player_choice = choices[int(player_input) - 1]
        computer_choice = random.choice(choices) 
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
