#Guess number game
#When the guess is correct u get a point
#Guessing number from 0 to 100


import random
score = 0

while True:
    num = random.randint(0, 100)

    guess = input('Enter the guess number [0-100] (or) [No] to exit the game: ').lower()

    if guess == 'no':
        break

    if not guess.isdigit():
        print('The guess can only be an integer')
        continue

    guess_conversion = int(guess)

    if guess_conversion == num:
        print('The guess is correct')
        print('You got a point')
        score += 1
        print(f'Your score is {score}')

    elif guess_conversion < num:
        print('The guess is low, Try again')

    elif guess_conversion > num:
        print('The guess is high, Try again')
