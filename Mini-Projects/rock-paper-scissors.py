##### V3 #######
from random import randint

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
print(f"Computer plays {computer}")

if player == "rock" or player == "paper" or player == "scissors":
    if player == "rock":
        if computer == "scissors":
            print("Player wins!")
        elif computer == "paper":
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
        elif computer == "scissors":
            print("Computer wins")
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!")
        elif computer == "paper":
            print("Player wins")
    else:
        print("it's a tie!")
else:
    print("You must chose between rock, paper, scissors..")

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
