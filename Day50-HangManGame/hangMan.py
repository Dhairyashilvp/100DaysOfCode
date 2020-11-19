import time
from random_word import RandomWords

name = input("Enter Your name: ")

print("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print("Start Guess....")
time.sleep(0.5)
r = RandomWords()
w = r.get_random_words()
word = w[0]
guesses = ""
turns = 10
while turns > 0:
    fail = 0
    for char in word:
        if char in guesses:
            print (char,end=" ")
        else:
            print("_",end=" ")
            fail+=1
    if fail == 0:
        print()
        print("you WON!")
        break
    print()
    guess = input("guess a character: ")
    guesses += guess
    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You LOOSE")
            print(word)