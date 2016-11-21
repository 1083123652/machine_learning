# -*- coding:utf-8 -*-
# sorted by insertion_sor by comparison


# Number in front of the numerical value and its comparison, to obtain the correct position
def INSERTION_SORT(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# getting data from file and transform
def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split(' ')
    for i in range(len(content)):
        data.append(float(content[i]))
    return data


if __name__ == '__main__':
    A = [3, 1, 9, 2, 4, 8, 5, 7, 6, 11]
    INSERTION_SORT(A)
    print A
