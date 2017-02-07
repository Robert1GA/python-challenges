# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calc_numbers():
    calc_operation = input('What calculation would you like to do? (add, sub, mult, div)?')
    number_1 = input('What is number 1? ')
    number_2 = input('What is number 2? ')
    if (calc_operation == 'add'):
        print('Your result is ', int(number_1) + int(number_2))
    elif (calc_operation == 'sub'):
        print('Your result is ', int(number_1) - int(number_2))
    elif (calc_operation == 'mult'):
        print('Your result is ', int(number_1) * int(number_2))
    elif (calc_operation == 'div'):
        print('Your result is ', int(number_1) / int(number_2))
    else:
        print('Your result is ', int(number_1) + int(number_2))

calc_numbers()
