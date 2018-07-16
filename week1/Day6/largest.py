import unittest
class Node:

    def __init__(self,data,nextNode=None,max=0):
        self.data = data
        self.nextNode = nextNode
        self.max = max

    def getData(self):
        return self.data

    def setData(self,val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,val):
        self.nextNode = val

class MaxStack(object):
    
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def push(self,data):
        if self.head is None:
            newNode = Node(data,self.head,data)
        else:
            newNode = Node(data,self.head,max(data,self.head.data))
        self.head = newNode
        self.size += 1
        return True
        
    def pop(self):
        try:
            x = self.head.data
            self.head = self.head.nextNode
            self.size -= 1
            return x
        except:
            return False
    
    def get_max(self):
        return self.head.max
    
    def getSize(self):
        return self.size

# Test Cases
max_stack = MaxStack()
max_stack.push(5)

actual = max_stack.get_max()
expected = 5
print(actual == expected)

max_stack.push(4)
max_stack.push(7)
max_stack.push(7)
max_stack.push(8)

actual = max_stack.get_max()
expected = 8
print(actual == expected)

actual = max_stack.pop()
expected = 8
print(actual == expected)

actual = max_stack.get_max()
expected = 7
print(actual == expected)

actual = max_stack.pop()
expected = 7
print(actual == expected)

actual = max_stack.get_max()
expected = 7
print(actual == expected)
