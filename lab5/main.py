import numpy as np

f = lambda x: (1 + 2 * (x ** 2) - x ** 3) ** (1 / 2)
a = 1.2
b = 2
eps = 0.0001
division_step = 2  # <--- this is 2n: step n = 1, 2*n = 2
partition_step = (b - a) / division_step
x_i = [a, a + partition_step, b]
f_i = [round(f(x_i[0]), 6), round(f(x_i[1]), 5), round(f(x_i[2]), 6)]
I_2 = round((partition_step / 3) * (f_i[0] + f_i[2] + 4 * f_i[1]), 6)  # initial result
print("The value of I_2: ", I_2)
division_step = 4
partition_step = (b - a) / division_step
x_i = [a, a + partition_step, a + 2 * partition_step, a + 3 * partition_step, b]
f_i = [round(f(x_i[0]), 6), round(f(x_i[1]), 6), round(f(x_i[2]), 6), round(f(x_i[3]), 6), round(f(x_i[4]), 6)]
I_4 = round((partition_step / 3) * (f_i[0] + f_i[4] + 2 * f_i[2] + 4 * f_i[1] + 4 * f_i[3]), 6)
print("The value of I_4: ", I_4)
dif = np.abs(I_4 - I_2)
if 1 / 15 * dif < eps:  # eps = 0.001
    print("the answer is: ", round(I_4, 3))