# Statistics are often calculated with varying amounts of input data. 
# Write a program that takes any number of non-negative floating-point numbers as input, 
# and outputs the max and average, respectively.

# Output the max and average with two digits after the decimal point.


def main():
    numbers = input().split()
    max_num = float(numbers[0])
    total = 0
    for num in numbers:
        num = float(num)
        if num > max_num:
            max_num = num
        total += num
    average = total / len(numbers)
    print(f'{max_num:.2f}')
    print(f'{average:.2f}')

if __name__ == '__main__':
    main()