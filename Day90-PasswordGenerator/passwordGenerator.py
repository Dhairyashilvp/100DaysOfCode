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

uppercaseList = [chr(i) for i in range(65,91)]
upper_char = getRandomzedList(uppercaseList,numberOfUpper)

lower_list = [chr(i) for i in range(97,123)]
lower_char = getRandomzedList(lower_list,numberOfLower)

digit_list = [str(i) for i in range(0,10)]
digit_char = getRandomzedList(digit_list,numberOfDigits)

sym_list = [chr(i) for i in range(33,48)]
sym_list +=[chr(i) for i in range (58,65)]
sym_list +=[chr(i) for i in range (91,97)]
sym_list +=[chr(i) for i in range (123,127)]
sym_char = getRandomzedList(sym_list,numberOfSym)

num_blank_char = numberOfChar - numberOfUpper - numberOfLower - numberOfDigits - numberOfSym
full_list = uppercaseList + lower_list + digit_list + sym_list
fillers_char = getRandomzedList(full_list,num_blank_char)


