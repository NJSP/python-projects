# Takes the total change amount in cents and calculates the change using the fewest coins
# Divides total change by 25 to get the number of quarters, then divides the remainder by 10 to get the number of dimes, etc.
def exact_change(total_change):
    if total_change <= 0:
        print('no change')
        quit()
    else:
        num_quarters = total_change // 25
        total_change %= 25
        num_dimes = total_change // 10
        total_change %= 10
        num_nickels = total_change // 5
        total_change %= 5
        num_pennies = total_change
        return num_pennies, num_nickels, num_dimes, num_quarters

# Reads the total change amount as an integer input, calls exact_change(), and outputs the change
if __name__ == '__main__':
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    if num_pennies > 1:
        print(f'{num_pennies} pennies')
    elif num_pennies == 1:
        print(f'{num_pennies} penny')
    if num_nickels > 1:
        print(f'{num_nickels} nickels')
    elif num_nickels == 1:
        print(f'{num_nickels} nickel')
    if num_dimes > 1:
        print(f'{num_dimes} dimes')
    elif num_dimes == 1:
        print(f'{num_dimes} dime')
    if num_quarters > 1:
        print(f'{num_quarters} quarters')
    elif num_quarters == 1:
        print(f'{num_quarters} quarter')