import math


def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def f(x):
    return (x**3) - math.sin(x) - 12 * x + 1


def df(x):
    return 4 * x**3 - 9 * x**2 - 40*x + 44


def dihotomia(a, b, func, ell):
    n = 0
    x_last = 0
    x_next = (a+b)/2
    asterio = (a+b)/ell
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
        x_next = (a+b)/2

    return x_next, n, asterio


def mod_newton(a, b, f, ell):
    x0 = b
    n = 0
    x = 0
    df_res = df(x0)

    while abs(x-x0) > ell or x0 <= a or x0 <= b:
        x = x0
        x0 = x0 - (f(x0) / df_res)
        n += 1
    return x0, n
