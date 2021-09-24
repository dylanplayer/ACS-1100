'''
Use while loops to solve the problems below.
'''


# TODO - Exercise 1: Repeatedly print the value of the variable price,
# decreasing it by 0.7 each time, as long as it remains positive.

from typing import Counter


price = 5

while price > 0:
    print(price)
    price -= 1


print("--------------")
# TODO - Exercise 2: Print ONLY even numbers from 0 to 20

for num in range(21):
    print(num)