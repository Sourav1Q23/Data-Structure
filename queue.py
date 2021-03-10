class Node(object):
    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None


class Queue(object):
    MAX_SIZE=10

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, x):
        newNode = Node(x)
        if self.head == None:
            self.head = self.tail = newNode
            self.length+=1
        elif self.length < Queue.MAX_SIZE:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.length += 1
        else:
            print("Queue is full")
            exit(1)
            
    def dequeue (self):
        item = self.head.item
        self.head = self.head.next 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def isEmpty(self):
        return True if self.length > 0 else False 