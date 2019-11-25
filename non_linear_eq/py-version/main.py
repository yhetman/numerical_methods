from algorithms import dihotomia
from algorithms import function
from algorithms import modificated_newton

func = function
ell = 10 ** -3
a = -0.9148
b = 4.7587
x, n, asterio = dihotomia(a, b, func, ell)
print("Метод дихотомії:\n x* = " + str(x) + "\n Апріорна оцінка: " + str(n) + "\n Астеріорна оцінка: " + str(asterio))
x, n = modificated_newton(a, b, func, ell)
print("Метод модифікований Ньютон:\n  x* = " + str(x) + "\n  Апріорна оцінка: " + str(n))
