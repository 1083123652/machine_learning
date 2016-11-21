# -*- coding:utf-8 -*-
# sortint data by count_sort


#Count sorting, each number in the array by calculation the number of occurrences of the sort
def COUNTING_SORT(A):
    B=[] #Save the array
    C=[] #The original array of possible values
    k=max(A)
    for i in range(len(A)):
        B.append(0)
    for i in range(k+1):
       C.append(0)
    for i in range(len(A)):
        C[A[i]]=C[A[i]]+1#the number of a numerical value
    for i in range(k):
        C[i+1]=C[i+1]+C[i]#Accumulated less than or equal to a numerical value,which stand for its position
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j] #The value placed on it in position
        C[A[j]]=C[A[j]]-1
    return B

# read data from filename and tranform into int data
def READ_FILE(filename):
    B=[]
    with open(filename) as f:
        content=f.read().strip().split(' ')
    for i in range(len(content)):
        B.append(int(content[i]))
    return B

if __name__=='__main__':
    A=[0,5,6,2,9,4,8,3,5,2,7,9,5,3,4,1,4,8,1,0,5,2,3,7]
    print len(A)
    B=COUNTING_SORT(A)
    print B

