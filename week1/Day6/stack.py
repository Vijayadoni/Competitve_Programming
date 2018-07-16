class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.inStack=[]
        self.outStack=[]

    # inStack=[]
    # outStack=[]
    def enqueue(self, item):
        while(self.inStack!=[]):
            self.outStack.append(self.inStack.pop())
        self.inStack.append(item)
        while(self.outStack!=[]):
            self.inStack.append(self.outStack.pop())

    def dequeue(self):
        if(self.inStack==[]):
            raise Exception
        else:
            return self.inStack.pop()