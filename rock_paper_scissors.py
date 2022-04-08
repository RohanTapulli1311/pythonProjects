import random

def play():
    print("Welcome, lets play rock paper scissors with computer!")
    choice = ['r','p','s']
    score_u = 0
    score_c = 0
    round = 1
    while round <= 3:
        print(f"Round {round}")
        user = input("ENTER YOUR CHOICE:'r' for rock,'p' for paper and 's' for scissors:")
        cp = random.choice(choice)
        if isWin(user,cp):
            score_u=score_u+1
            print('User wins this round!')
            print(f"Current points are: User = {score_u} and Computer = {score_c}")
        else:
            score_c=score_c+1
            print('Computer wins this round!')
            print(f"Current points are: User = {score_u} and Computer = {score_c}")
        round=round+1
    if score_c < score_u:
        print("User wins the Game!")
    else:
        print("Hard Luck, Try again next time!")

def isWin(u, cp):
    if (u=='r' and cp=='s') or (u=='p' and cp == 'r') or (u=='s' and cp =='p'):
        return True
    else:
        return False

play()