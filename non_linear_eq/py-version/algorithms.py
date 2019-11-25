import math


def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def function(x):
    return (x**3) + math.sin(x) - 12 * x + 1


def dfunction(x):
    return 3 * x * x + math.cos(x) - 12


def dihotomia(a, b, func, ell):
    n = 0
    x_last = 0
    x_next = (a + b) / 2
    asterio = (a + b) / ell
    asterio = math.log2(asterio)
    asterio = math.fabs(asterio) + 1
    asterio = int(asterio)

    while abs(x_next - x_last) > ell:

        x_last = x_next

        if sgn(func(a)) == sgn(func(x_last)):
            a = x_last
        if sgn(func(b)) == sgn(func(x_last)):
            b = x_last

        n += 1
        x_next = (a + b) / 2

    return x_next, n, asterio


def modificated_newton(a, b, func, ell):
    x0 = b
    n = 0
    x = 0
    df = dfunction(x0)

    while abs(x-x0) > ell or x0 <= a or x0 <= b:
        x = x0
        x0 = x0-(func(x0)/df)
        n += 1
    return x0, n
