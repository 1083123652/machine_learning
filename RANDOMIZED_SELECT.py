# -*- coding:utf-8 -*-
# RANDONISED SELECT
# The case of small numerical I randomly selected array
# using the randomized partition of quicksort method
from random import randint


# At last numerical [r] A as standard
def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    # grouping
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            (A[i], A[j]) = (A[j], A[i])
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# Random number selection criteria
def RANDOMIZED_PARTITION(A, p, r):
    i = randint(p, r)
    (A[r], A[i]) = (A[i], A[r])
    return PARTITION(A, p, r)


# Returns A [p.. r] in the case of small number I
def RANDOMIZED_SELECT(A, p, r, i):
    if p == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p + 1  # K for A array [p.. r] in the first k small number, is A [q]
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q - 1, i)
    else:
        return RANDOMIZED_SELECT(A, q + 1, r, i - k)


# Get the data source from the file
# Format conversion
def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split()
    for i in range(len(content)):
        data.append(int(content[i]))
    return data


if __name__ == "__main__":
    A = [2, 15, 26, 8, 9, 16, 7, 23, 32, 4, 17, 28, 34]
    B = A[:]
    prompt = "please input the number for select:\n"
    input = raw_input(prompt)
    input = int(input)
    result = RANDOMIZED_SELECT(A, 0, len(A) - 1, input)
    print B
    print result
