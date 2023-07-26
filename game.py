import random

# Start of our game
def gamestart():
    # Our main part of the game is rock, paper, scissors
    options = ("rock", "paper", "scissors")
    player = input("Enter your choice (rock, paper, scissors): ")
    computer = random.choice(options)

    # Check for a tie
    if player == computer:
        print("It's a tie!")

    # Win game part
    elif player == "rock" and computer == "scissors":
        print("You win! Computer selected scissors!")
    elif player == "paper" and computer == "rock":
        print("You win! Computer selected rock!")
    elif player == "scissors" and computer == "paper":
        print("You win! Computer selected paper!")

    # Defeat part of the game
    elif player == "rock" and computer == "paper":
        print("You lose! Because computer selected paper!")
    elif player == "paper" and computer == "scissors":
        print("You lose! Because computer selected scissors!")
    elif player == "scissors" and computer == "rock":
        print("You lose! Because computer selected rock!")

    return_game = input("Do you want to play again (y/n)? ")
    if return_game == 'y':
        gamestart()
    elif return_game == 'n':
        print("Thanks for your gameplay!")

# Call the function to start the game
gamestart() 