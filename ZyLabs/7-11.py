# takes a character and a string as input, converts the string into a list of words, 
# and prints the words that contain the character

letter = input()
words = input().split(' ')

for i in words:
    if letter in i:
        print(i+',', end='')
        