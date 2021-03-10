class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class Doublylinkedlist:
    def __init__(self):
        self.head= None
    
    def insert(self,value):
        if self.head == None:
            self.head= Node(value)
        else:
            newNode= Node(value)
            curr= self.head
            while curr.next:
                curr=curr.next
            curr.next= newNode
            newNode.prev = curr
    def delete(self,value):
        if self.head.value ==value:
            self.head = self.head.next
            self.head.prev = None
            return

        curr= self.head.next
        while not curr == None and not curr.value == value:
            curr=curr.next
        if curr == None:
            return "Value not found"
        elif curr.next == None:
            curr.prev.next =None
        else:
            curr.prev.next= curr.next
            curr.next.prev= curr.prev
            return "Value Deleted"

    def search(self,value):
        curr = self.head
        while curr:
            if curr.value == value:
                return curr.value
            curr = curr.next

    def print(self):
        curr = self.head
        while curr:
            print (curr.value)
            curr = curr.next
ll = Doublylinkedlist()
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.print()
ll.delete(8)
ll.print()
            