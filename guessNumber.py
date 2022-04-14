import random

def guess(x):
    rand = random.randint(1,x)
    guess = 0
    while guess!= rand:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < rand:
            print("Guess again!, your guess is too low")
        elif guess>rand:
            print("Guess again! your guess is too high")
    print(f"Found the number {rand} correctly!")
    
def computer_guess(x):
    userNum = int(input(f"Enter a number between 1 and {x} which should be guessed by computer:"))
    c_guess = 0
    low =1
    high=x
    while c_guess!= userNum:
        
        c_guess = random.randint(low,high)
        if c_guess < userNum:
            print(f"computer guessed {c_guess}, which is low. trying again!")
            low = c_guess
        elif c_guess > userNum:
            print(f"computer guessed {c_guess}, which is high. trying again!")
            high = c_guess
    print(f"Computer guessed the number {userNum} correctly!!")



guess(10)
computer_guess(10)
