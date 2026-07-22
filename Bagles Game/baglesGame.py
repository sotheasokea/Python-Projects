import random

#a normal instruction printed function
def instruction():
    print("Bagels, a deductive logic game.")
    print("\nI am Thinking of a 4-digit positive number. Try to guess what it is.")
    print("Here are some clues:")
    print("\nWhen I say: That means:")
    print("+ Pico       One digit is correct but in the wrong direction.")
    print("+ Fermi      One digit is correct and in the right position.")
    print("+ Bagels     No digit is correct.")
    print("\nI have thought up a number.")
    print("-> You have 15 guesses to get it.\n")

#it's better to : secretNumber = f"{random.randint(0, 9999):04d}"
def getRandomNumber():
    number = random.randint(0, 9999)
    return f"{number:04d}"

#printing the clue for each guess
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

#output the instruction of the game
instruction()

secretNumber = getRandomNumber()
maxGuesses = 1      # maxGuesses=10, it starts at 1
result = "Try Again"

#looping when player guessing the number
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

#show the answer if player can't guess correctly
if result == "Try Again":
    print("\nThe secret number was:", secretNumber,"☠️\n")


