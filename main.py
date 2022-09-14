# Author: Michael Fessler
# Datum: 14.9.2022
# Version: 0.1

import math

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
operator = str(input("Enter Operator: "))
if operator == "+":                                             # if else construct to select
    result = str(num1 + num2)                                   # the desired arithmetic operations
    print("Result of the addition is: " + result)               # addition
elif operator == "-":                                           # subtraction
    result = str(num1 - num2)
    print("Result of the subtraction is: " + result)
elif operator == "*":                                           # multiplication
    result = str(num1 * num2)
    print("Result of the multiplication is: " + result)
elif operator == "/":                                           # division
    result = str(num1 / num2)
    print("Result of the division is: " + result)
elif operator == "e":                                           # exponentiation
    result = str(num1 ** num2)
    print("Result of the exponentiation is: " + result)
elif operator == "s":                                           # square root
    result = str(math.sqrt(num1))
    print("Result of the square root is: " + result)
elif operator == "sml":                                         # smallest value
    if num1 > num2:                                             # nested if else construct to identify smallest
        print("Smallest number is: " + str(num2))
    elif num1 < num2:
        print("Smallest number is: " + str(num1))
elif operator == "lrg":                                         # largest value
    if num1 > num2:                                             # if else construct to identify largest
        print("Largest number is: " + str(num1))
    elif num1 < num2:
        print("Largest number is: " + str(num2))
elif operator == "abs":                                         # absolute value
    print("The absolute value of Number One (" + str(num1) + ") is: " + str(abs(num1)))
    print("The absolute value of Number Two (" + str(num2) + ") is: " + str(abs(num2)))
elif operator == "mean":                                        # mean value
    result = str((num1 + num2) / 2)
    print("The mean value of " + str(num1) + " and " + str(num2) + " is: " + result)
