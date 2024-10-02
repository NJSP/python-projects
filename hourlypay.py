#variables
hours = None
rate = None

print('please input how many hours you work per week.')
hours = float(input('hours:'));

print('please input your hourly rate.')
rate = float(input('rate:'))

pay = hours * rate
print('your weekly pay is ' + str(pay))
