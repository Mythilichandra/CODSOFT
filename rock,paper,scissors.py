import random
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")


    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round.")
            computer_score += 1

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Play another round? (yes/no): ").strip().lower()
        
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
        round_num += 1

if __name__ == "__main__":
    play_game()