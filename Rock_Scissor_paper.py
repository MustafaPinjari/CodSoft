import random

choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0

def display_result(player, computer):
    print(f"\nYour choice: {player}\nComputer's choice: {computer}")
    
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return f"You win! {player} beats {computer}"
    else:
        return f"You lose! {computer} beats {player}"

while True:
    print("\nRock, Paper, or Scissors? (Type 'End' to finish)")
    player = input().capitalize()

    if player == 'End':
        print("\nFinal Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break

    elif player not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer = random.choice(choices)
    result = display_result(player, computer)

    if "win" in result:
        player_score += 1
    elif "lose" in result:
        cpu_score += 1

    print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nFinal Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break