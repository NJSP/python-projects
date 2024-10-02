# (1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)

# (2) Complete the get_num_of_characters() function, which returns the number of characters 
# in the user's string. We encourage you to use a for loop in this function. (2 pts)

# (3) Extend the program by calling the get_num_of_characters() function and then output the 
# returned result. (1 pt)

# (4) Extend the program further by implementing the output_without_whitespace() function. 
# output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs).
# Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)
# Ex:

# Enter a sentence or phrase: 
# The only thing we have to fear is fear itself.

# You entered: The only thing we have to fear is fear itself.

# Number of characters: 46
# String with no whitespace: Theonlythingwehavetofearisfearitself.



def get_num_of_characters(input_string):
    count = 0
    for i in input_string:
        count += 1
    return count

def output_without_whitespace(input_string):
    nospace = ''
    for i in input_string:
        if i != ' ' and i != '\t':
            nospace += i
    return nospace

if __name__ == '__main__':
    input_string = input('Enter a sentence or phrase:\n')
    print('\nYou entered:', input_string)
    print('\nNumber of characters:', get_num_of_characters(input_string))
    print('String with no whitespace:', output_without_whitespace(input_string))