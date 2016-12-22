# -*- coding:utf-8 -*-
# learning KNN of machine learning for Supervised learning
# principle: Find the input data and K in the sample closest
# to the data, and finally, select the K most similar to the most
#  frequently occurring data classification

from numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    #tile(A, reps) --Construct an array
    # by repeating A the number of times given by reps.
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=add.reduce(sqDiffMat,axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    # Returns the indices that would sort an array.
    classCount={}
    for i in range(k):
        voteIlable=labels[sortedDistIndicies[i]]
        classCount[voteIlable]=classCount.get(voteIlable,0)+1

    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    # operator.itemgetter(1)---Get the first few fields
    # print sortedClassCount
    # print sortedClassCount[0][0]
    return sortedClassCount[0][0]

if __name__=='__main__':
    group,labels=createDataSet()
    inx=[0,0.2]
    classify0(inx,group,labels,3)


