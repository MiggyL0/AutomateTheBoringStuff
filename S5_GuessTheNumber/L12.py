# This is a guess the number game.
import random

print('Hello, what is your name?')
name = input()

print ('Well ' + name + ' I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

# print('DEBUG: Secret number is: ' + str(secretNumber))

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Nope, too low')
    elif guess > secretNumber:
        print('Nope, lol too high!!')
    else:
        break # This is only possible if they correctly guess

if guess == secretNumber:
    print('Great job, ' + name + ' you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, I was thinking of ' + str(secretNumber) + '.')