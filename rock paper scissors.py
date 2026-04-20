import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Rock Paper Scissors! Type 'q' to quit.")

while True:
    player = input("Enter your choice (rock, paper, scissors): ").lower().strip()

    if player == 'q':
        break 

    if player not in choices:
        print("Invalid choice! Try rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print(f"you chose: {player}")
    print(f"computer chose: {computer}") 

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print(f"Final score - You: {player_score}, Computer: {computer_score}")

print("Thanks for playing!")