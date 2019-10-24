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
    for j in range(0, n):
        q = A[::-1, j]
        '''for k in range(0,j):
            print(f"La division es: {producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k])}")
            print(f"Y se multiplica por: {A[::-1, k]}")
            print(f"El resultado es {(producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k])) * A[::-1, k]}")
            print(f"Todo se resta a {A[::-1,j]}")
            A[::-1, j] -= (producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k])) * A[::-1, k]

            print(f"Este e  s el vector columa resultante: {A[:,j]}\n")'''
        for k in range(j):
            print(f"La division es: {producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k])}")
            print(f"Y se multiplica por: {A[::-1, k]}")
            print(f"El resultado es {(producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k])) * A[::-1, k]}")
            rij = producint(A[::-1, j], A[::-1, k]) / producint(A[::-1, k], A[::-1, k]) * A[::-1, k]
            q = q - rij
            A[::-1, j] = q
    return A


def producint(f1, f2):
    integral = np.polyint(P.polymul(f1, f2))
    value = (np.polyval(integral, 1) - np.polyval(integral, -1))
    return value


if __name__ == '__main__':
    g = int(input("ingrese el grado maximo de los polinomios"))
    r = int(input("ingrese el numero de polinomios"))
    mat = Lectura(r, g)

    print(mat)
    print(gram_schmidt(sep_column(mat)))


