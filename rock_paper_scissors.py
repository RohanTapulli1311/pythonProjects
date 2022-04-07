import random

def play():
    print("Welcome, lets play rock paper scissors with computer!")
    user = input("ENTER YOUR CHOICE:'r' for rock,'p' for paper and 's' for scissors:")
    choice = ['r','p','s']
    cp = random.choice(choice)
    score_u = 0
    score_c = 0
    