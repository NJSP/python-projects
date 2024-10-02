# Given two integers that represent the number of strokes used and par, write a program that prints 
# the appropriate score name. Print "Error" at the end of the output if par is not 3, 4, or 5, or if the 
# score's name is not "Eagle", "Birdie", "Par", or "Bogey".

strokes = int(input())
par = int(input())
score = ''

eagle = par-2
birdie = par-1
bogey = par+1

if par in [3, 4, 5]:
    if strokes == eagle:
        score = 'Eagle'
    elif strokes == birdie:
        score = 'Birdie'
    elif strokes == par:
        score = 'Par'
    elif strokes == bogey:
        score = 'Bogey'
    else:
        score = 'Error'
else:
    score = 'Error'

print(f'Par {par} in {strokes} strokes is {score}')