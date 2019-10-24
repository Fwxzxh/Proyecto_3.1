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
    for j in range(n):
        for k in range(j):
            #A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
            print(f"Esto es v: {A[::-1, j]}")
            print(f"Esto es u:  {A[::-1,k]}")
            print("\n")

            integral = np.polyint(P.polymul(A[::-1, j], A[::-1, k]))
            print(f"Esta es la multiplicacion de v*u: {P.polymul(A[::-1, j], A[::-1, k])}")
            print(f"Esta es la integral de v*u: {integral}")
            integral2 = np.polyint(P.polymul(A[::-1, k], A[::-1, k]))
            print(f"Esta es la multiplicacion de u*u: {P.polymul(A[:, k], A[:, k])}")
            print(f"Esta es la integral de u*u: {integral2}")
            print("\n")
            print(f"La integral definida de v*u es:{np.polyval(integral, 1) - np.polyval(integral, -1)}")
            print(f"La integral definida de u*u es:{np.polyval(integral2, 1) - np.polyval(integral2, -1)}")
            print(f"Esta es la division de las integrales: {(np.polyval(integral, 1) - np.polyval(integral, -1)) / (np.polyval(integral2, 1) - np.polyval(integral2, -1))}")
            print("\n")
            A[:, j] -= ((np.polyval(integral, 1) - np.polyval(integral, -1)) / (np.polyval(integral2, 1) - np.polyval(integral2, -1))) * A[:, k]
            print(f"Este es el vector columa resultante: {A[:,j]}\n")
    return A


if __name__ == '__main__':
    g = int(input("ingrese el grado maximo de los polinomios"))
    r = int(input("ingrese el numero de polinomios"))
    mat = Lectura(r, g)
    print(mat)
    print(gram_schmidt(sep_column(mat)))


