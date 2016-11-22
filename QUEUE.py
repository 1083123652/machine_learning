# -*- coding:utf-8 -*-
# Simulation of the Queue

class Queue():
    """simulation of the Queue"""
    def __init__(self,size):
        self.size=size
        self.items = []
        self.front=-1
        self.rear=-1

    def isFull(self):
        return self.rear-self.front+1==self.size

    def isEmpty(self):
        return self.front==self.rear

    def enqueue(self,item):
        if self.isFull():
            raise Exception("queue is full")
        else:
            self.items.append(item)
            self.rear+=1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue is empty")
        else:
            self.front+=1
            # return self.items.pop(0)
            return self.items[self.front]

    def size(self):
        return len(self.items)

if __name__=="__main__":
    q=Queue(20)
    for i in range(5):
        q.enqueue(i)
    print q.dequeue()
    print q.dequeue()
    print q.isEmpty()


