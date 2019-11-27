import numpy as np
from algorithm import triagonal_algo
from algorithm import Jacobi


def init_mat():
    size = int(input("Input matrix size: "))
    print("-------------------------------------------------------")
    if size < 3:
        raise ArithmeticError

    mat = np.zeros((size, size))
    value = 0
    f = []


    print("-------------------------------------------------------")
    print("\t\tINITIALIZE THE MATRIX")
    print("-------------------------------------------------------")
    for i in range(size):
        for j in range(size):
            string = "Set element [" + str(i) + "][" + str(j) + "]: "
            value = float(input(string))
            mat[i][j] = value

    for i in range(size):
        value = float(input("Set f[" + str(i) + "]: "))
        f.append(value)

    return mat, f


def wrong_dim():
    print("-------------------------------------------------------")
    print("  ERROR! The dimension must be greater or equal to 3")
    print("-------------------------------------------------------")


def results_out():
    print("-------------------------------------------------------")
    print("\t\tHERE ARE THE RESULTS")
    print("-------------------------------------------------------")


def main():
    mat = 0
    f = 0

    method = 1
    while True:

        print("\n-------------------------------------------------------")
        print ("Available options :")
        print("\t\tTridiagonal matrix algorithm\tpress 1")
        print ("\t\tJacobi algorithm\t\tpress 2")
        print("\t\tTo exit\t\t\t\tpress 3")
        print("-------------------------------------------------------")
        print("\n-------------------------------------------------------")
        method = int(input("Choose which method to use : "))
        print("-------------------------------------------------------")
        if method == 1:
            
            try:
                mat, f = init_mat()
            except ArithmeticError:
                wrong_dim()
                break

            results_out()
            x, res = thomas_algorithm(mat, f)
            print("X :\n" + str(x) + '\n' + "Det :\n\t" + str(res) + '\n')
        
        elif method == 2:
            
            try:
               mat, f = init_mat()
            except ArithmeticError:
               wrong_dim()
               break

            x = [0, 0, 0]
            ell = float(input("Enter ellipsis: "))
            x, res = Jacobi(mat, f, x, ell)
            results_out()
            print("X :\n" + str(x) + '\n' + "Num :\n\t" + str(res) + '\n')

        elif method == 3:

            break

        else:
            print("-------------------------------------------------------")
            print ("\t  Oops... Invalid input! Try again!")
            print("-------------------------------------------------------")
            continue

main()
