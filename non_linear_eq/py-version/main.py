from math_algoritms import dihotomia
from math_algoritms import f
from math_algoritms import mod_newton

func = f
ell = 10 ** -3
a = -0.9148
b = 4.7587
x, n, asterio = dihotomia(a, b, func, ell)
print("Метод дихотомії:\n x* = " + str(x) + "\n Апріорна оцінка: " + str(n) + "\n Астеріорна оцінка: " + str(asterio))
x, n = mod_newton(a, b, func, ell)
print("Метод модифікований Ньютон:\n  x* = " + str(x) + "\n  Апріорна оцінка: " + str(n))
