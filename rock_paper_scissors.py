import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

first_to_ask = input("Do you want to play the game? [yes] or [no]")

def play_the_game():


    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again.")

    computer_num = random.randint(1,3)
    computer_move = ""
    if computer_num == 1:
        computer_move = rock
    elif computer_num ==2:
        computer_move = paper
    elif computer_num == 3:
        computer_move = scissors

    print(f"Computer chose is {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? [yes] or [no]")
    if play_again == "yes":
        play_the_game()
    else:
        print("Have a great day!")


if first_to_ask == "yes":
    play_the_game()
else:
    print("Have a great day!")