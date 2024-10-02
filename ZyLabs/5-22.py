# Write a program that first gets a list of integers from input. 
# The input begins with an integer indicating the number of integers that follow. 
# Then, get the last value from the input, which indicates a threshold. Output all integers 
# less than or equal to that last threshold value.

listlen = int(input())
mylist = []
li = None
newlist = ''

while len(mylist) <= listlen:
    li = int(input())
    mylist.append(li)
    if len(mylist) == listlen:
        break
maxnum = int(input())

for i in mylist:
    if i <= maxnum:
        newlist += str(i) + ', '
    else:
        continue
print(newlist)
