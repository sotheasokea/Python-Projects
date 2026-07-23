# birthday the same as long as day and date the same. (year isn't important)

from datetime import date, timedelta
import random

# introduction
def introduction():
    print(
'''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
    ''')

# generating a list of random birthday
def generateBirthday(numberOfBirthday):
    birthdays = []

    # change startYear to any date you want ( same birthday -> year is unimportant )
    for i in range(numberOfBirthday):
        startOfYear = date(2001, 1, 1)
        # get a random day
        randomNumberOfDays = timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays

        birthdays.append(birthday)
    return birthdays

# check for matching birthday
def getMatchBirthday(birthdays):

    # if all birthday are the unique return none
    if len(birthdays) == len(set(birthdays)):
        return None

    # compare each birthday
    for indexA, birthdayA in enumerate(birthdays):
        for indexB, birthdayB in enumerate(birthdays[indexA+1 :]):
            if birthdayA == birthdayB:
                return birthdayA


introduction()

# tuple for 12 months
MONTHS = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
)
# input a valid value 1 - 100
while True:
    print('How many birthday shall I generate? (Max 100)')
    inputNumber = input('> ')
    if inputNumber.isdecimal() and (0 < int(inputNumber) <= 100):
        numBDays = int(inputNumber)
        break
print()

# generate and output the numBDays birthdays

print('Here are', numBDays, 'birthdays:')
birthdays = generateBirthday(numBDays)
# print(type(birthdays))
# print(birthdays[0])
# print(birthdays[0].month)
# print(birthdays[0].day)
# print('-----')
for index, birthday in enumerate(birthdays):
    if index != 0:
        print(', ', end='')
    print(MONTHS[birthday.month-1], birthday.day, end='')
print('\n')

# checking the matching birthdays in those generated birthdays
match = getMatchBirthday(birthdays)
# print(match)
if match != None:
    print('multiple people have a birthday on',MONTHS[match.month -1],match.day)
else:
    print('there are no matching birthdays.')
print()

# run 100, 000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # number of simulations that have the matching birthday
for i in range(100_000):
    # report on every 10, 000 simulations
    if i % 10_000 == 0:
        print(i, 'simulation run...')

    birthdays = generateBirthday(numBDays)
    if getMatchBirthday(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')
print()
# display simulations results:
probability = round(simMatch/100_000*100, 2)
print('Out of 100, 000 simulations of',numBDays,'people, there was a')
print('matching birthday in that group',simMatch,'times. This means')
print('that',numBDays,'people have a ',probability,'% chance of')
print('having a matching birthday in their group.\n')
print('That\'s probably more than you would think!🫣\n')
