'''
Name:Delaina Poppleton
Date: 9/24/24
Description: more on f-strings, input, and numbers
'''

my_int = 5
my_float = 6.38
print(f"{my_int} {my_float}")

another_float = 8.0
float_two = float(8)
print(f"{another_float} {float_two}")

# get a decimal from a user
radius = float(input("enter a radius: "))
print(f"you entered a radius of {radius}")

# operations on numbers
# P E MModD AS
# modulus operator or remainder operator
print(15 % 7) # prints the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, times 4

# exponent is not ^ , it is **
print(5**4) # this is 5 to the 4th
print(5^4) # this is not

# weird math stuff'
print(0.3-0.2) #roundoff error - watch out for it

# rounding
# method 1, use round()
num = 3.1415
print(round(num,2))
# method 2, use f string
print(f"{num:.2f}")

#your turn to code
# ask a user for some amount of US dollars
# store this in a variable
# convert that money to some currency of your choice
# store the conversion factor in a variable
# store the final amount in a variable
# print it like "___ USD is the same as ___ CAD"
# Round to 2 decimal places

USD = float(input("enter amount of USD: "))
conversion_factor = 0.90
euros = usd*conversion_factor
rounded_euros = round(euros,2)
print(f"{USD}USD is the same as {rounded_euros}CAD")

# String methods
name = "lee cat"
print(name.upper())
print(name.title())
print(name2.lower())


