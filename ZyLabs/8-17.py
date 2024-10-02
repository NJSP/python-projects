# Statistics are often calculated with varying amounts of input data. 
# Write a program that takes any number of non-negative floating-point numbers as input, 
# and outputs the max and average, respectively.

# Output the max and average with two digits after the decimal point.


def max_and_ave(lst):
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    return 'Max: ' + str(max(lst)) + ', Average: ' + str(round(sum(lst)/len(lst), 2))


text = input()
split_text = text.split(' ')

print(max_and_ave(split_text))

