# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. 
# The input is a string to represent the month and an int to represent the day.

input_month = input()
input_day = int(input())

m = input_month.lower()
months = {'january': 31, 'february': 29, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july':31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
wint = ['january', 'february']
spr = ['april', 'may']
summ = ['july', 'august']
fall = ['october', 'november']

if m in months and (0 < input_day <= months[m]):
    for month in months:
        if m == month:
            if m == 'march':
                if input_day < 20:
                    print('Winter')
                else:
                    print('Spring')
            elif m == 'june':
                if input_day < 21:
                    print('Spring')
                else:
                    print('Summer')
            elif m == 'september':
                if input_day < 22:
                    print('Summer')
                else:
                    print('Autumn')
            elif m == 'december':
                if input_day < 21:
                    print('Autumn')
                else:
                    print('Winter')
            elif m in wint:
                print('Winter')
            elif m in spr:
                print('Spring')
            elif m in summ:
                print('Summer')
            elif m in fall:
                print('Autumn')
        else:
            continue
else:
    print('Invalid')
