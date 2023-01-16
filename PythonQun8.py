
import random
number = random.randint(1,9)
guess = 0

while guess != number :
    guess = int(input("Please guess your number between 1 and 9, including both of them : ")) 
    if guess == number:
        print("You guessed it correct!")
    elif guess > number :
        print("Too high!") 
    else : 
        print("Too low !")
        