num_list=[]

count = 1
while len(num_list) < 4:
    num_list.append(float(input(f'Enter weight {count}:\n')))
    count += 1

print('Weights:', num_list)
print('')
print(f'Average weight: {sum([float(num) for num in num_list])/len(num_list):.2f}')
print(f'Max weight: {max([float(num) for num in num_list]):.2f}')
print('')
location = (int(input('Enter a list location (1 - 4):\n')))
print(f'Weight in pounds: {float(num_list[location-1]):.2f}')
print(f'Weight in kilograms: {float(num_list[location-1]) / 2.2:.2f}')
print('')
print('Sorted list:', sorted(num_list))