'''
Name: Delaina Poppleton
Date: 10/1/24
Description: Unit 2 homework 1
'''

print('Problem 1'.center(20,'-'))



print('Problem 2'.center(20,'-'))

print('Problem 3'.center(20,'-'))

distance_seattle = 173.8
miles_per_gallon = float(input("how many miles per gallon does your car get? "))
price_of_gas = float(input("how much is a gallon of gas near your home? "))
gallon_of_gas = float(input("how many gallons of gas does your car hold? "))

miles_per_tank = miles_per_gallon*gallon_of_gas 
if miles_per_tank == 173.8:
    total_cost = gallon_of_gas*price_of_gas 
    print(f"The cost to drive to seattle is ${total_cost}")
elif miles_per_tank > 173.8:
     total_cost = gallon_of_gas*price_of_gas
     print(f"The cost to drive to seattle is ${total_cost}")
elif miles_per_tank < 173.8:
    total_cost = gallon_of_gas*price_of_gas*2
    print(f"The cost to drive to seattle is ${total_cost}")


