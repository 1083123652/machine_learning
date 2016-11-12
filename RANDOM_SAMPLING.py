# -*- ccoding:utf-8 -*-
# random sampling
# adapting to quicksort
from random import randint


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            (A[i], A[j]) = (A[j], A[i])
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def RANDOMIZED_PARTITION(A, p, r):
    i = randint(p, r)
    (A[r], A[i]) = (A[i], A[r])
    return PARTITION(A, p, r)


def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q - 1)
        RANDOMIZED_QUICKSORT(A, q + 1, r)


def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split()
    for i in range(len(content)):
        data.append(int(content[i]))
    return data


if __name__ == '__main__':
    data = READ_DATA('data.txt')
    print data
    RANDOMIZED_QUICKSORT(data, 0, len(data) - 1)
    print data
