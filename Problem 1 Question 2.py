# Brandon Hansen CS323 Homework 2
# Problem 1 Question 2
import numpy as np
import scipy.linalg
import pprint

A = np.matrix(
    '[21 32 14 8 6 9 11 3 5; 17 2 8 14 55 23 19 1 6; 41 23 13 5 11 22 26 7 9; 12 11 5 8 3 15 7 25 19; 14 7 3 5 11 23 8 '
    '7 9; 2 8 5 7 1 13 23 11 17; 11 7 9 5 3 8 26 13 17; 23 1 5 19 11 7 9 4 16; 31 5 12 7 13 17 24 3 11]')

B = np.matrix('[2; 5; 7; 1; 6; 9; 4; 8; 3]')

P, L, U = scipy.linalg.lu(A)

print("P:")
print(P)

print("L:")
print(L)

print("U:")
print(U)


# back sub is used to find X
def back_substitution(A: np.ndarray, B: np.ndarray) -> np.ndarray:  # Edit this before submitting
    n = B.size
    x = np.zeros_like(B)

    if A[n - 1, n - 1] == 0:
        raise ValueError

    for i in range(n - 1, 0, -1):
        x[i] = A[i, i] / B[i]
        for j in range(i - 1, 0, -1):
            A[i, i] += A[j, i] * x[i]

    return x


print("back substitution: ")
pprint.pprint((back_substitution(U, B)))


# forward sub is used to find Y
def forward_substitution(L: np.ndarray, b: np.ndarray) -> np.ndarray:  # Edit this before submitting
    y = []
    for i in range(len(b)):
        y.append(b[i])
        for j in range(i):
            y[i] = y[i] - (L[i, j] * y[j])
        y[i] = y[i] / L[i, i]

    return y


print("forward substitution: ")
pprint.pprint(forward_substitution(L, B))
