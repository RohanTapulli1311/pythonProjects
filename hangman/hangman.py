import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    lives =6
    word = getValidWord(words)
    word_letters = set(word) #letters in word
    alphabets = set(string.ascii_uppercase)
    used_letters = set() #to store letters used by user

    #getting user letters
    while len(word_letters) >0 and lives>0:
        #letters used 
        print("You have ",lives," lives left and You have used these letter:",''.join(used_letters))
        #What current word is (ie W-RD)
        #print(word)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word:",' '.join(word_list))
        user_letter = input("Enter a letter:").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
        elif user_letter in used_letters:
            print("You have already used this letter")
        else:
            print("invalid character!")
    if(lives == 0):
        print("Sorry you died, the word was:",word)
    else:
        print(f"You guessed the word {word} correctly!!")

hangman()







