red = input()
green = input()
blue = input()
cval = [int(red), int(green), int(blue)]

gray = min(cval)

cval = [item - gray for item in cval]

print(cval[0],cval[1],cval[2])
