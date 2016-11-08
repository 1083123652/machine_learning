# -*- coding:utf-8 -*-
# MERGE SORT
import sys
sys.setrecursionlimit(1000000)

def Merge(data, first_index, median_index, last_index):
    n1 = median_index - first_index + 1
    n2 = last_index - median_index
    L = []; R = []
    for i in range(n1):
        L.append(data[first_index+i])
    for i in range(n2):
        R.append(data[median_index+i+1])
    L.append(99)
    R.append(99)
    i = 0; j = 0
    for k in range(first_index,last_index+1):
        if L[i] < R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j +=1


def Merge_Sort(data, first_index, last_index):
    if first_index < last_index:
        median_index = int((last_index+first_index)/2)
        Merge_Sort(data, first_index, median_index)
        Merge_Sort(data, median_index+1, last_index)
        Merge(data, first_index, median_index, last_index)


def ReadData(filename):
    data = []
    with open(filename) as f:
        temp = f.read()
    temp = temp.split(" ")
    for i in range(len(temp)):
        data.append(int(temp[i]))
    return data

if __name__ == "__main__":
    unsortedData = ReadData('data.txt')
    unsortedData = [2,5,8,3,1,6]
    print unsortedData
    Merge_Sort(unsortedData, 0, len(unsortedData)-1)
    print unsortedData



