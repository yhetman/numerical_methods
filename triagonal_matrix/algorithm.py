import calculations as calc


def enter_x_arr(lam, beta, x, size):

    len = size - 2
    val = -1

    # x_i = beta_i + lambda_i * x_i+1

    for i in range(len, val, val):
        value = beta[i] + lam[i] * x[abs(i - len)]
        x.append(value)

    return x


def det_mat(c, z):
    res = c

    #det = c1 * z2 * .... * zn

    for i in range(0, len(z)):
        res *= z[i]

    return res


def triagonal_algo(mat, f):
    c_dia = calc.sort_diagonal(mat)
    a_dia = calc.sort_diagonal(mat, n = 1, p = 1)
    b_dia = calc.sort_diagonal(mat, k = 1, p = 1)
    size = len(mat[0])
    x = []
    lam, beta, z, value = calc.prepare_lam_beta_z_and_x_n(c_dia, a_dia, b_dia, f)
    x.append(value)
    x = enter_x_arr(lam, beta, x, size)
    x = calc.reinversion_vector_x(x)
    res = det_mat(c_dia[0], z)
    return x, res


def init_r(mat):
    r = []
    size = len(mat[0])
    for i in range(size):
        r.append(1/mat[i][i])

    return r


def summary(mat, i, x):
    size = len(mat[0])
    sum = 0

    for j in range(size):
        if j == i:
            continue
        sum += mat[i][j] * x[j]

    return sum


def Jacobi(mat, b, x, ell):
    x_arr = [x]
    x = []
    j = 1

    r = init_r(mat)
    size = len(mat[0])

    for i in range(size):
        x.append(r[i] * (b[i] - summary(mat, i, x_arr[0])))

    x_arr.append(x)
    x = []

    while calc.vector_module(x_arr[j], x_arr[j-1]) > ell:
        for i in range(3):
            x.append(r[i] * (b[i] - summary(mat, i, x_arr[j])))
        x_arr.append(x)
        x = []
        j += 1

    try:
        num = calc.condition_number(mat)
    except Exception:
        num = "Error"

    return x_arr[len(x_arr)-1], num
