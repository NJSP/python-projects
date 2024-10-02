# Program to check if the input is a number or not

num = input()

for i in num:
    try:
        int(i)
        continue
    except:
        print('No')
        break
else:
    print('Yes')