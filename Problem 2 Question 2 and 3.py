# Brandon Hansen CS323 Homework 2
# Problem 2 Question 2 and 3
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy


def func(x):  # This function is getting a value at a specific point of the equation
    val = math.exp(math.cos(x) + math.cos(x ** 2)) + math.cos(x) - 1
    return val


print("Initial Guess f(0):       " + str(func(0)))
print("Initial Guess f(1):       " + str(func(1)))
print("Initial Guess f(2):       " + str(func(2)))
print("----------------------------")


def bisection(f, a, b, max_iters, eps):  # This is doing the bisection method
    if f(a) * f(b) >= eps:
        print("error: could not use bisection method")
        exit()

    iters = 0
    c = 0.5 * (a + b)
    steps = []
    roots = []
    while abs(f(c)) >= eps:
        steps.append(iters)
        roots.append(c)
        iters += 1  # Works as a counter for how many iterations it takes to converge
        # print(iters + round(f(c), 4))
        print(str(iters) + " Iterative Step: " + str(round(f(c), 4)))
        if f(a) * f(c) < 0.:
            # Search (a,c)
            a = a
            b = c
            c = 0.5 * (a + b)
        elif f(c) * f(b) < 0:
            a = c
            b = b
            c = 0.5 * (a + b)
    print("----------------------------")
    print("The value of midpoint: " + str(round(c, 4)))
    print("The value of midpoint at f(c): " + str(f(c)))
    print("iterations: {}".format(iters))
    plt.plot(steps, roots)
    plt.xlabel("Step Number")
    plt.ylabel("absalute value of f(x_k)")
    plt.show()


bisection(f=func, a=0, b=2, max_iters=100, eps=1e-6)
