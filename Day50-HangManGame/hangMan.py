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
