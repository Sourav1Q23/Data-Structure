class Node:
    MAX_SIZE=10
    def __init__(self,value):
        self.value= value
        self.prev=None
        self.next=None

class Stack:
    MAX_SIZE=10
    def __init__(self):
        self.head=None
        self.rear=None
        self.size=0
    def isEmpty(self):
        return True if self.size > 0 else False

    def peek(self):
        if self.rear:
            return self.rear.value
        else:
            return "Stack Is Empty "

    def push(self,value):
        if self.size < Stack.MAX_SIZE:
            if self.head is None:
                node = Node(value)
                self.head=self.rear= node
                self.size=1
            else:
                node= Node(value)
                self.rear.next= node
                node.prev = self.rear
                self.rear = node
                self.size += 1

        else:
            return " Stack is Full"

    def pop(self):
        if self.rear is  None:
            return "Stack Is Empty "

        elif self.rear == self.head:
            val = self.rear.value
            self.rear = self.head = None
            self.size=0
        else:
            val = self.rear.value
            self.rear.prev.next = None
            self.rear.prev = None
            self.size-=1
            return val
