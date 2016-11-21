# -*- coding:utf-8 -*-
# sortint data by index_sort


# To obtain the maximum number of bits in the array
def GET_INDEX_NUMBER(A):
    index = 1
    max_data = max(A)
    remainder = max_data // 10
    while remainder != 0:
        index += 1
        remainder = remainder // 10
    return index


# Count sorting, each number in the array by calculation the number of occurrences of the sort
def COUNTING_SORT(A, data):
    B = []  # Save the array
    C = []  # The original array of possible values
    k = max(A)
    for i in range(len(A)):
        B.append(0)
    for i in range(k + 1):
        C.append(0)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1  # the number of a numerical value
    for i in range(k):
        C[i + 1] = C[i + 1] + C[i]  # Accumulated less than or equal to a numerical value,which stand for its position
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = data[j]  # The value placed on it in position
        C[A[j]] = C[A[j]] - 1
    return B


# Radix sort, through the study of the count of every digital sequence (from bits to the highest)
def INDEX_SORT(A):
    temp = A[:]
    B = A[:]
    index = GET_INDEX_NUMBER(A)
    for i in range(1, index + 1):
        for j in range(len(A)):
            temp[j] = B[j] % pow(10, i)
            temp[j] = temp[j] / pow(10, i - 1)
        B = COUNTING_SORT(temp, B)
        print B#print sorting process
    return B


# read data from filename and tranform into int data
def READ_FILE(filename):
    B = []
    with open(filename) as f:
        content = f.read().strip().split(' ')
    for i in range(len(content)):
        B.append(int(content[i]))
    return B

# testing
if __name__ == '__main__':
    A = [329, 457, 657, 839, 436, 720, 355]
    print INDEX_SORT(A)
