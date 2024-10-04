# Takes a list of numbers and prints the middle number

mylist = input().split()

if len(mylist) > 9:
    print('Too many inputs')
    quit()
else:
    mysplit = int(len(mylist) / 2)
    print('Middle item:',mylist[mysplit])