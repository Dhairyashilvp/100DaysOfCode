import random

def getRandomzedList(inputList, number):
    randomzedList = []
    for i in range (number):
        randomzedList.append(random.choice(inputList))
    return randomzedList

while True:
    numberOfChar = int(input('Entet the Number of charecters you want in your Password : '))
    numberOfUpper = int(input('What is the least number of UPPERCASE letters needed in your Password? : '))
    numberOfLower = int(input('What is the least number of lowercase letters needed in your Password? : '))
    numberOfDigits = int(input('What is the least number of Digits needed in your Password: '))
    numberOfSym = int(input('What is the least number of Symbols in your Password: '))

    if numberOfChar < numberOfUpper + numberOfLower + numberOfDigits + numberOfSym:
        print('The number of charecters are lesser then required')
    else:
        break



