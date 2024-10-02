#Write a function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon, 
# and miles_driven, that returns the dollar cost to drive those miles. All items are of 
# type float. The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

# Define that function in a program whose inputs are the car's miles per gallon and the 
# price of gas in dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles, 
# and 400 miles, by calling your driving_cost() function three times.

#Output each floating-point value with two digits after the decimal point, 
# which can be achieved as follows:
#print(f'{your_value:.2f}')

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    mpg = float(input())
    dpg = float(input())
    print(f'{driving_cost(mpg, dpg, 10):.2f}')
    print(f'{driving_cost(mpg, dpg, 50):.2f}')
    print(f'{driving_cost(mpg, dpg, 400):.2f}')