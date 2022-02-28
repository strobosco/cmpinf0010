import random

chosenRange = int(input("How may numbers do you wanna guess from?"))

randomNum = random.randint(0, chosenRange)
guess = int(input("Guess a number: "))
count = 1
while guess != randomNum:
    guess = int(input("Guess a number: "))
    count += 1

print("It took you ", count, " guesses to find the correct number.")