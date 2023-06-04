import numpy as np
from math import inf

def gaussseidel(ite, tol, K, F):
    # ite: max number of iterations
    # tol: tolerance
    # K: stiffness matrix, after applying boundary conditions
    # F: force vector, after applying boundary conditions
    U = np.zeros(len(F))
    relative_error = inf
    for iteration in range(ite):
        U_new = U.copy()  # Initialize U_new as a copy of U
        for i in range(len(F)):
            U[i] = (F[i] - np.dot(K[i,:],U) + K[i,i]*U[i]) / K[i,i]
        relative_error = np.linalg.norm(U - U_new) / np.linalg.norm(U)
        if abs(relative_error) < tol:
            break
    return U, relative_error, iteration

F = np.array([0, 150, -100])
K = (10**8) * np.array([[1.59, -0.4, -0.54], [-0.4, 1.7, 0.4], [-0.54, 0.4, 0.54]])

U, relative_error, iterations = gaussseidel(ite=100, tol=1e-6, K=K, F=F)
print("U = ", U)
print("Relative error = ", relative_error)
print("Number of iterations = ", iterations)