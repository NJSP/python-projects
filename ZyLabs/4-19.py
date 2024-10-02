# Write a program that takes in a year and determines whether that year is a leap year.

is_leap_year = False
   
year = int(input())

if year%100 == 0:
    if year%400 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
elif year%4 == 0:
    is_leap_year = True

if is_leap_year == True:
    print(f'{year} - leap year')
else:
    print(f'{year} - not a leap year')


