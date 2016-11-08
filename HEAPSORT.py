# -*- coding:utf-8 -*-
# Heap sorting
# using heapsort for sorting data

# Gets the parent node
def PARENT(i):
    return (i + 1) / 2 - 1


# Gets the left child node
def LEFT(i):
    return 2 * i + 1


# Gets the right child node
def RIGHT(i):
    return 2 * i + 2


# To achieve the maximum heap
# Gets the maximum value of the parent node and child nodes
def MAX_HEAPIFY(A, i):
    left = LEFT(i)
    right = RIGHT(i)
    if left <= A_heap_size - 1 and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right <= A_heap_size - 1 and A[right] > A[largest]:
        largest = right
    if largest != i:
        (A[i], A[largest]) = (A[largest], A[i])
        MAX_HEAPIFY(A, largest)  # Ensure that the heap node of the heap to maximize


# Build the heap sequence
# An array of size n, with n / 2 through n being leaf nodes
def BUILD_MAX_HEAP(A):
    global A_heap_size
    A_heap_size = len(A)
    for i in range(len(A) / 2 - 1, -1, -1):
        MAX_HEAPIFY(A, i)


# Creates a heap sort
def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    global A_heap_size
    A_heap_size = len(A)
    for i in range(len(A) - 1, 0, -1):
        (A[0], A[i]) = (A[i], A[0])
        A_heap_size = A_heap_size - 1
        MAX_HEAPIFY(A, 0)


# Get the data source from the file
def READ_DATA(filename):
    data = []
    with open(filename) as f:
        content = f.read().strip().split(' ')
    for i in range(len(content)):
        data.append(int(content[i]))
    return data


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 24, 53]
    BUILD_MAX_HEAP(A)
    print A
    HEAPSORT(A)
    print A
