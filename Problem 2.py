# Brandon Hansen CS323 Homework 2 Problem 2
import math
import matplotlib.pyplot as plt


# define the objective function
def func(x):
    # cubic function with 3 roots when == 0.: 1, 2, 3
    # val = (x - 1.) * (x - 2.) * (x - 3.)
    val = math.exp(math.cos(x) + math.cos(x ** 2)) + math.cos(x) - 1
    return val


print("Initial Guess at f(0): " + str(round(func(0), 4)))
print("Initial Guess at f(1): " + str(round(func(1), 4)))
print("Initial Guess at f(2): " + str(round(func(2), 4)))
print("----------------------")


def bisection(f, a, b, max_iters, eps):
    if f(a) * f(b) >= eps:
        print('error: could not use bisection method!')
        exit()
    # otherwise: bisection method works on (a, b)
    iters = 0
    c = 0.5 * (a + b)
    steps = []
    roots = []

    while abs(f(c)) >= eps and iters < max_iters:
        steps.append(iters)
        roots.append(c)
        if f(a) * f(c) < 0.:
            # search (a, c)
            a = a
            b = c
            c = 0.5 * (a + b)
        elif f(c) * f(b) < 0:
            # search (c, b)
            a = c
            b = b
            c = 0.5 * (a + b)
        iters += 1
        print(str(iters) + " Iterative Step: " + str(abs(round(f(c), 4))))

    # print('{}: {}'.format(c, f(c)))
    print("----------------------")
    print("The root at f(x) = 0 is: " + str(round(c, 4)))
    print('iterations: {}'.format(iters))
    plt.plot(steps, roots)
    plt.xlabel("k")
    plt.ylabel("|f(x_k)|")
    plt.show()


bisection(f=func, a=0., b=2., max_iters=10000, eps=1e-6)
