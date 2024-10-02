import random as ra

# Variables
num = ra.randint(0, 100)
guess = None
attempts = 1
diff = None
range = None


print('Welcome to the super fun number guessing extravaganza!')

# Takes user input to set difficulty. Also checks to make sure the input is one of the acceptable options
while True:
    diff = input('To begin, please choose your difficulty: easy, medium, hard \n')
    if diff == 'easy':
        num = ra.randint(0, 10)
        range = '0 and 10'
        break
    elif diff == 'medium':
        num = ra.randint(0, 50)
        range = '0 and 50'
        break
    elif diff == 'hard':
        num = ra.randint(0, 100)
        range = '0 and 100'
        break
    else:
        print("That is not an acceptable response.\n")


print("I'm thinking of a number between " + range +". Try to guess what it is!")

# Handles input for guesses, adds 1 to the total number of guesses until the the correct number is guessed, and scolds the player if they input something other than an integer
while True:
    try:
        guess = int(input())
        if guess == num:
            print('correct! It took you ' + str(attempts) + ' attempts!')
            break
        elif guess > (num + 10):
            print('much lower!')
            attempts += 1
        elif guess > num:
            print('a little lower')
            attempts += 1
        elif guess < (num - 10):
            print('much higher!')
            attempts += 1
        else:
            print('a little higher!')
            attempts += 1
    except:
            print("This input only accepts integers.")