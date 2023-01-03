#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# if the number is greater than 0: is positive
if number > 0:
    print("{:d} is positive".format(number))
# if the number is 0: is zero
elif number == 0:
    print("{:d} is zero".format(number))
# if the number is less than 0: is negative
else:
    print("{:d} is negative".format(number))
