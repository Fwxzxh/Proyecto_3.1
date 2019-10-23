import re
import numpy as np
import math
from numpy.polynomial import polynomial as P
from scipy.integrate import quad

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
    for j in range(n):
        for k in range(j):
            #A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
            A[:, j] -= quad(P.polymul(A[:, k], A[:, j]), -1, 1) *A[:, k]
        A[:, j] = A[:, j] / quad(P.polymul(A[:, j], A[:, j]), -1, 1)
    return A


def TeoremaFun(f, a, b):
    integral = f(b)-f(a)
    return integral


if __name__ == '__main__':
    g = int(input("ingrese el grado maximo de los polinomios"))
    r = int(input("ingrese el numero de polinomios"))
    mat = Lectura(r,g)
    print(mat)
    print(sep_column(mat))
    print(gram_schmidt(sep_column(mat)))