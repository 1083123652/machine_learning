# -*- coding:utf-8 -*-
# matrix calculation

from numpy import *
def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
    n = len(A)
    C = array([[0 for i in range(n)]]*n)
    if n == 1:
        C[n-1,n-1] = A[n-1,n-1] * B[n-1,n-1]
    else:
        C[0:n/2,0:n/2] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0:n/2,0:n/2], B[0:n/2,0:n/2]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0:n/2,(n+1)/2:],
                                                                                                        B[(n+1)/2:,0:n/2])
        C[0:n/2,(n+1)/2:] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0:n/2,0:n/2], B[0:n/2,(n+1)/2:]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[0:n/2,(n+1)/2:],
                                                                                                        B[(n+1)/2:,(n+1)/2:])
        C[(n+1)/2:,0:n/2] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[(n+1)/2:,0:n/2], B[0:n/2,0:n/2]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[(n+1)/2:,(n+1)/2:],
                                                                                                        B[(n+1)/2:,0:n/2])
        C[(n+1)/2:,(n+1)/2:] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[(n+1)/2:,0:n/2], B[0:n/2,(n+1)/2:]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[(n+1)/2:,(n+1)/2:],
                                                                                                        B[(n+1)/2:,(n+1)/2:])
    return C

if __name__ == '__main__':
    A  =array([[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]])
    B = array([[2, 4, 5, 7],
               [5, 3, 1, 2],
               [6, 6, 8, 1],
               [3, 2, 3, 6]])

    C = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A,transpose(B))
    # n=4
    # print A[0:n/2,0:n/2],A[0:n/2,(n+1)/2:]
    # print A[0,0]
    # C = array([[0 for i in range(n)] ]* n)
    print C
    # n=4
    # print n,n/2,(n+1)/2

