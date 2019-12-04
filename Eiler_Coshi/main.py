import matplotlib.pyplot as plt


def y_der_func(x, y, z):
    return pow(x, 1 / 2) + pow(y, 1 / 2) * pow(z, 1 / 3)


def z_der_func(x, z, y):
    return 5 * pow(x, 1 / 5) + 2 * pow(y, 1 / 4) * pow(z, 1 / 2)


def koshi_euler():
    container_for_x = [0]
    container_for_y = [1]
    container_for_z = [1]
    h = 1
    for i in range(1, 10):
        container_for_y.append(container_for_y[i - 1] +
                               h * y_der_func(container_for_x[i - 1],
                                              container_for_y[i - 1],
                                              container_for_z[i - 1]))
        container_for_z.append(container_for_z[i - 1] +
                               h * z_der_func(container_for_x[i - 1],
                                              container_for_z[i - 1],
                                              container_for_y[i - 1]))
        container_for_x.append(container_for_x[i - 1] + h)

    plt.plot(container_for_x, container_for_y, label="y'")
    plt.plot(container_for_x, container_for_z, label="z'")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    return


koshi_euler()

