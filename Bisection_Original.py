import math
import matplotlib.pyplot as plt


# define the objective function
def func(x):
    # cubic function with 3 roots when == 0.: 1, 2, 3
    # val = (x - 1.) * (x - 2.) * (x - 3.)
    val = math.exp(math.cos(x) + math.cos(x ** 2)) + math.cos(x) - 1
    return val


# print(func(0.))
# print(func(1.5))
# print(func(2.5))
# print(func(5))

def bisection(f, a, b, max_iters, eps):
    if f(a) * f(b) >= eps:
        print('error: could not use bisection method!')
        exit()
    # otherwise: bisection method works on (a, b)
    iters = 0
    c = 0.5 * (a + b)
    steps = []
    roots = []
    '''
        Note that the max_iters was dismissed in the video.
        It can be used as another stop criteria 
    '''
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
        print(str(iters) + " Iterative Step: " + str(round(f(c), 4)))

    print('{}: {}'.format(c, f(c)))
    print('iterations: {}'.format(iters))
    plt.plot(steps, roots)
    plt.show()


# print(func(-2))
# print(func(-1))
# print(func(1))
# print(func(2))
# print(func(3))
bisection(f=func, a=0., b=2., max_iters=10000, eps=1e-6)
