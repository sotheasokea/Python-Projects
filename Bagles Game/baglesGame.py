import random


def instruction():
    print("Bagels, a deductive logic game.")
    print("Recoded by Sothea Sokea")
    print("\nI am Thinking of a 4-digit positive number. Try to guess what it is.")
    print("Here are some clues:")
    print("\nWhen I say: That means:")
    print("+ Pico       One digit is correct but in the wrong direction.")
    print("+ Fermi      One digit is correct and in the right position.")
    print("+ Bagels     No digit is correct.")
    print("\nI have thought up a number.")
    print("-> You have 15 guesses to get it.\n")

def getRandomNumber():
    number = random.randint(0, 9999)
    return f"{number:04d}"

def getClue(guessNumber, secretNumber):
    if guessNumber == secretNumber:
        return "You got it!";
    clues = []
    for i in range(len(guessNumber)):
        if guessNumber[i] == secretNumber[i]:
            clues.append("Fermi")
        elif guessNumber[i] in secretNumber:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)

instruction()

secretNumber = getRandomNumber()
maxGuesses = 1
result = "Try Again"
while True:
    userGuess = input(f"Guess #{maxGuesses}: ")
    if len(userGuess) < 4:
        userGuess = userGuess.zfill(4)
    userGuess = userGuess[:4]
    print(userGuess)
    maxGuesses += 1
    result = getClue(userGuess, secretNumber)
    print(result)
    if (result == "You got it!"):
        break;
    if maxGuesses > 15:
        result = "Try Again"
        break;

if result == "Try Again":
    print("\nThe secret number was:", secretNumber,"☠️\n")


