# Brandon Hansen CS323 Homework 2
# Problem 1 Question 3
import numpy as np
from numpy import sqrt

A = np.array([
    (21, 32, 14, 8, 6, 9, 11, 3, 5), (17, 2, 8, 14, 55, 23, 19, 1, 6), (41, 23, 13, 5, 11, 22, 26, 7, 9),
    (12, 11, 5, 8, 3, 15, 7, 25, 19), (14, 7, 3, 5, 11, 23, 8,
                                       7, 9), (2, 8, 5, 7, 1, 13, 23, 11, 17), (11, 7, 9, 5, 3, 8, 26, 13, 17),
    (23, 1, 5, 19, 11, 7, 9, 4, 16), (31, 5, 12, 7, 13, 17, 24, 3, 11)])

transpose_of_A = np.matrix.transpose(A)
A_transpose_times_A = transpose_of_A * A

eignevalues = np.linalg.eig(A_transpose_times_A)
print(eignevalues)

largest_eigen = 1555.13189375
print("The Largest eigenvalue of A^T*A: 1555.13189375")
print("L2 Norm: " + str(sqrt(largest_eigen)))
