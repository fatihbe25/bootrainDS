"""
 1.Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value.
 What would be your money at the end of a week if you had invested $1000
 with an average daily increase of 12% ? You can solve the problem using Python.
"""
import math

capital = 1000
daily_growth = 12
period = 7

final_growth_rate = 1.12 ** 7
result = capital * (1.12 ** 7)

print(result)

"""
2. Print the text in quotes with Python.
 However, you must get the numbers from variables using .format() notation.
Because the text is long, you might consider writing in two lines:
"""

print(
    "When we buy bitcoin with {} USD at the beginning of the week,\nwe would earn {:.2f} USD at the end of the week, with an average gain of {}\%.".format(
        capital, result - capital, daily_growth))

"""
3. Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. 
For conversion, you can use this formula: C = (5/9) * (F - 32)

"""
F = input("Enter the temperature in Fahrenheit: ")
C = (5/9) * (float(F)-32)
print("Temperature (C) : {:.2f}".format(C))

"""
4. Get a three digit number the from user and calculate the sum of the digits in the integer.
"""

number = input("Enter a three digit number: ")
digit_1 = int(number[0])
digit_2 = int(number[1])
digit_3 = int(number[2])
sum_of_digits = digit_1 + digit_2 + digit_3

print("The sum of digits in the number is {}".format(sum_of_digits))

"""
 5. Write some code to calculate the hypotenuse of a right angled triangle.
    Get the side lengths from the user.
"""
a = input("first side length : ")
b = input("second side length: ")
c = math.sqrt(int(a)**2 + int(b)**2)
print("The length of the hypotenuse is {:.0f}".format(c))

