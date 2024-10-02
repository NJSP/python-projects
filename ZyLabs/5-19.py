# ZyLabs 5.19
# Write a program that takes in an integer in the range 11-99 (inclusive) as input. 
# The output of the program is a countdown starting from the input integer until an integer where 
# both digits are identical.

unum = int(input())
if 11 <= unum <= 99:
    if str(unum)[1] == str(unum)[0]:
        print(unum)
        quit()
else:
    print('Input must be 11-99')
    quit()  
while True:
    print(unum)
    unum -= 1
    if str(unum)[1] == str(unum)[0]:
        print(unum)
        break
    continue
