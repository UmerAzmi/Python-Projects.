import random

print('Welcome to Random Number Guesser.')

while True:
    try:
        top_of_range = int(input('Enter the range of number you want to guess within from 0 to ? '))
        if top_of_range <= 0:
            print('Please enter a number greater than 0')
        else:
            break
    except:
        print('Please enter a numeric value.')

random_number = random.randint(0, top_of_range)

number_of_guesses = 0

while True:
    number_of_guesses += 1
    try:
        user_input = int(input('\nEnter your guess: '))
        if user_input <= 0:
            print('Please enter a number greater than 0')
        if user_input == random_number:
            print('You guessed right!')
            break
        if user_input > random_number:
            print('Your guess is higher than the number!.')
        if user_input < random_number:
            print('Your guess is lower than the number!.')
    except:
        print('Please enter a numeric value.')

print('\nIt took you {} guesses.'.format(number_of_guesses))
print('Thank you for playing!')
