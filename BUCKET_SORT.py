# -*- coding:utf-8 -*-
# sorted by bucket_sort

# Number in front of the numerical value and its comparison, to obtain the correct position
def INSERTION_SORT(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# The first group within the group ordering
def BUCKET_SORT(A):
    n = len(A)
    B = []
    C=[]
    for i in range(n):
        B.append([])
    for i in range(n):
        B[int(n * A[i])].append(A[i])  # group
    for i in range(n):
        INSERTION_SORT(B[i])
    for i in range(n):
        if B[i]:
            for j in range(len(B[i])):
                C.append(B[i][j])
    return C


# getting data from file and transform
def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split(' ')
    for i in range(len(content)):
        data.append(float(content[i]))
    return data


if __name__ == "__main__":
    A = [0.28, 0.17, 0.39, 0.26, 0.22, 0.94, 0.21, 0.12, 0.23, 0.68]
    B = BUCKET_SORT(A)
    print B
