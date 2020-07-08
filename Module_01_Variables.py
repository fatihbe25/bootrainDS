"""
1. Define two variables as x and y.
   Assign 1 to x and '1' to y. Then check if two variables have the same value and type.
"""
x, y = 1, '1'
print("x == y => {}".format(x == y))
print("x type is {}, y type is {}".format(type(x), type(y)))

"""
 2. Change the type of variable y and make the two variables the same.  
"""

print("x == y => {}".format(x == int(y)))