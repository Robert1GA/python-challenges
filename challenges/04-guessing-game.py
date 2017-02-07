from random import randint

MIN = 1
MAX = 100

def guessing_game():
    set_number = randint(MIN, MAX)
    guess_attempt = 0
    print(set_number)
    guess = int(input("Guess a number between %d and %d: " % (MIN, MAX)))
    if (guess > set_number):
        print('The number is lower than %d. Guess again' % (guess))
        guess_attempt += 1
    elif (guess < set_number):
        print('The number is lower than %d. Guess again' % (guess))
        guess_attempt += 1
    elif (guess == set_number):
        print('You got it correct!  It took you %d guesses' % (guess_attempt))

guessing_game()
