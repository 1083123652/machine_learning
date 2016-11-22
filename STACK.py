# -*- coding:utf-8 -*-
# Simulation of the stack

class Stack():
    """simulation of the stack"""

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = []

    def isFull(self):
        return self.top + 1 == self.size

    def isEmpty(self):
        return self.top == -1
        # return len(self.items) == 0

    def push(self, item):
        if self.isFull():
            raise Exception("out of range")
        else:
            self.items.append(item)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]


if __name__=="__main__":
    s=Stack(20)
    for i in range(3):
        s.push(i)
    print s.pop()
    print s.pop()
    for i in range(3,5):
        s.push(i)
    print s.pop()
    print s.pop()
    print s.isEmpty()