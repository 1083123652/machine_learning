# -*- coding:utf-8 -*-
# QUIK_SORT
# Site sorting

# The size comparison is performed with the last element as a reference
# entain A[p..q-1]<A[q]<A[q+1..r]
# Where A[b] is the original array of A[r]
def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# The first simple sort, in the recursive
def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)  # simple sort,reserved A[q]
        QUICKSORT(A, p, q - 1)  # recursive
        QUICKSORT(A, q + 1, r)  # recursive


# Get the data source from the file
# Format conversion
def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split(' ')
    for i in range(len(content)):
        data.append(int(content[i]))
    return data


if __name__ == '__main__':
    A=READ_DATA('data.txt')
    print A
    QUICKSORT(A, 0, len(A) - 1)
    print A
