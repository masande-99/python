import random


def guessing():
    number = random.randint(1, 10)
    number_of_guesses = 0

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break


guessing()

