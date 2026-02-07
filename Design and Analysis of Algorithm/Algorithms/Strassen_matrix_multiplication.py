# Strassen's matrix multiplication
import numpy as np

def strassen(A, B):
    n = A.shape[0]

    # Base case
    if n == 1:
        return A * B

    # Divide matrices into 4 submatrices
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Strassen's 7 multiplications
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Combine results
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine submatrices
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))

    return C


# Example
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(strassen(A, B))
