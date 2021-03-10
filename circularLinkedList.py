class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Circularlinkedlist:
    def __init__(self):
        self.head= None
        
    def insert(self, value):
        if self.head ==None:
            newNode = Node(value)
            newNode.next = newNode
        else:
            newNode = Node(value)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            newNode.next = self.head
            curr.next = newNode
    def search(self, value):
        if self.head.value == value:
            return value

        curr = self.head.next
        while not curr == self.head:
            if curr.value == value:
                return value
            curr= curr.next
        return "Value Not Found"

    def delete(self, value):
        # value is equal to self.head.value
        if self.head.value == value:
            if self.head == self.head.next:
                self.head=None
            else:
                curr = self.head
                if not curr.next == self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head.next = None
                self.head = curr.next
        else:
            curr= self.head
            prev=None
            while curr.next != self.head:
                prev= curr
                curr = curr.next
                if curr.value == value:
                    prev.next= curr
                    curr.next = None
                    break


        


        
