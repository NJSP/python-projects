#Write a program that reads a list of integers into a list as long as the 
# integers are greater than zero, then outputs the 
# smallest and largest integers in the list.

num = None
num_list = []

while True:
    num = int(input())
    if num > 0:
        num_list += [num]
    else:
        break

if len(num_list) == 0:
    quit()
elif len(num_list) == 1:
    print(num_list[0])
else:
    print(min(num_list), 'and', max(num_list))