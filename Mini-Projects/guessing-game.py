import random

random_number = random.randint(1, 10) 
guess = None

while True:
  guess = int(input("Pick a number form 1 to 10: "))
  if guess > random_number:
    print("Too high!")
  elif guess < random_number:
    print("Too low!")
  else: 
    print("You got it!")
    play_again = input('Do you want to play again? (y/n)')
    if play_again == "y":
      random_number = random.randint(1, 10) 
      guess = None
    else:
     print("Thank you for playing!")
     break

