##### V3 #######
from random import randint
player_wins = 0
computer_wins = 0
while player_wins < 2 and computer_wins < 2:
    print(f"Player score: {player_wins} | Computer score: {computer_wins}")
    print("Rock..")
    print("Paper..")
    print("Scissors..")

    rand_num = randint(0, 2)

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print("Player, make your move:")
    player = input().lower()

    if player == "quit" or player == "q":
      break

    print(f"Computer plays {computer}")

    if player == "rock" or player == "paper" or player == "scissors":
        if player == "rock":
            if computer == "scissors":
                print("Player wins!")
                player_wins += 1
            elif computer == "paper":
                print("Computer wins!")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player wins!")
                player_wins += 1
            elif computer == "scissors":
                print("Computer wins")
                computer_wins += 1
        elif player == "scissors":
            if computer == "rock":
                print("Computer wins!")
                computer_wins += 1
            elif computer == "paper":
                print("Player wins")
                player_wins += 1
        else:
            print("it's a tie!")
    else:
        print("You must chose between rock, paper, scissors..")
if player_wins > computer_wins:
  print("Congrats, you won!")
elif player_wins == computer_wins:
  print("It's a tie..")
else: 
  print("Oh no, computer won.. :(")
print(f"FINAL SCORE... Player score: {player_wins} | Computer score: {computer_wins} ")
##### v2 #####
# print("Rock..")
# print("Paper..")
# print("Scissors..")

# print("Player 1, make your move:")
# player1 = input()
# print("Player 2, make your move:")
# player2 = input()

# if player1 == "rock":
#     if player2 == "scissors":
#         print("player 1 wins!")
#     elif player2 == "paper":
#         print("Player 2 wins!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("Player 1 wins!")
#     elif player2 == "scissors"
#     print("Player 2 wins")
# elif player1 == "scissors":
#     if player2 == "rock":
#         print("Player 2 wins!")
#     elif player2 == "paper":
#         print("Player 1 wins")
# else:
#     print("Oops, something went wrong")

######## V1 ########
# if player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("Player 2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("Player 2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("Player 1 wins!")
# elif player1 == player2:
#     print("Its a tie!")
# else:
#     print("Something went wrong")
