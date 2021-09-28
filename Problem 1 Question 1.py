# Brandon Hansen CS323 Homework 2
# Problem 1 Question 1
import numpy
import numpy as np
import pprint

# Declaring A Matrix
A = np.matrix(
    '21 32 14 8 6 9 11 3 5; 17 2 8 14 55 23 19 1 6; 41 23 13 5 11 22 26 7 9; 12 11 5 8 3 15 7 25 19; 14 7 3 5 11 23 8 '
    '7 9; 2 8 5 7 1 13 23 11 17; 11 7 9 5 3 8 26 13 17; 23 1 5 19 11 7 9 4 16; 31 5 12 7 13 17 24 3 11')
# Declaring B Matrix
B = np.matrix('2; 5; 7; 1; 6; 9; 4; 8; 3')

# This try else statement checks to see if the Matrix is invertible, if it is, invert it
try:
    np.linalg.inv(A)
except numpy.linalg.LinAlgError:
    print("Not Invertible")
else:
    np.linalg.inv(A)

# Declaring A as A^-1B
X = np.linalg.inv(A) * B
# Printing X
print("A^-1 * B = ")
pprint.pprint((X.round(4)))
