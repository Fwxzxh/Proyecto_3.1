import numpy as np
from numpy.polynomial import polynomial as P


def Lectura(r,g):

    MatO = np.zeros((r, g))
    for i in range(r):
        for j in range(g):
            MatO[i, j] = float(input(f"ingrese el valor del polinomio {i+1} en x{j}"))
    return MatO


def sep_column(mat):
    vect1 = []
    for j in range(g):
        vect1.append(mat[:, j])
    vec = np.array(vect1)
    return vec


def gram_schmidt(A):
    n = A.shape[1]  # numero de vectores columna
    buffer = A[::-1, 0]
    for j in range(n):  # 0,1,2 numero de vectores
        for k in range(j):  # j = 0. 0,1. 0,1,2 numero de restas
                if k < 1:
                    buffer =  producint(A[::-1, k], A[::-1, j]) / producint(A[::-1, k], A[::-1, k]) * A[::-1, k]
                else:
                    buffer1 = (producint(A[::-1, k], A[::-1, j]) / producint(A[::-1, k], A[::-1, k])) * A[::-1, k]
                    buffer = buffer - buffer1
        if (j>=1):
            A[::-1, j] =  A[::-1, j] - buffer
    return A


def producint(f1, f2):
    integral = np.polyint(np.polymul(f1, f2))
    value = (np.polyval(integral, 1) - np.polyval(integral, -1))
    return value


if __name__ == '__main__':
    #B = np.array([[1,2,1],[0,1,-1,],[0,0,1]], np.float)
    #print(gram_schmidt(B))
    g = int(input("ingrese el grado maximo de los polinomios"))
    r = int(input("ingrese el numero de polinomios"))
    mat = Lectura(r, g)
    print(mat)
    print(gram_schmidt(sep_column(mat)))