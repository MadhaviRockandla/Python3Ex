"""
Exercise 2
Create a program called higher_or_lower.py
The program must meet the following criteria.
- A function that asks the user to provide a number between 0 and 10.
- A function that returns a random number between 1 and 10.
- A function that evaluates the randomly generated number against the user's guess.
- At the end, the program must output the following:
    - The random number that was generated.
    - The user's guess.
    - An indication if the user guess correctly or if the user's guess was too high/too low.
Answer below:
"""
"""File named higher_or_lower.py is created separately."""

def guess_function():
    guess = input('Guess a number between 0 and 10: ')
    return int(guess)

def randnum_function():
    from random import randrange
    return randrange(10)

def evaluate():
    guess_number = guess_function()
    rand_number = randnum_function()
    if guess_number > rand_number:
        result='Too High'
    elif guess_number < rand_number:
        result='Too Low'
    else:
        result='Equal'
    print('The random number was ' + str(rand_number))
    print('The number guessed was ' + str(guess_number))
    print('Your guess was ' + str(result))

evaluate()