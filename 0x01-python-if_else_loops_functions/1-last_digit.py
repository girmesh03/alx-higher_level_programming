#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check if number is negative, if so, get last digit and make it negative
if number < 0:
    # get last digit
    last_digit = number % -10
else:
    # get last digit
    last_digit = number % 10

# print last digit
print("Last digit of {:d} is {:d} and is ".format(number, last_digit), end="")

# if the last digit is greater than 5
if last_digit > 5:
    print("greater than 5")
# if the last digit is 0:
elif last_digit == 0:
    print("0")
# if the last digit is less than 6 and not 0:
else:
    print("less than 6 and not 0")
