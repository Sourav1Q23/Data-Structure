class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class linkedlist:
    
    def __init__(self):
        self.head=None
    
    
    def insert(self,value):
        if not self.head:
            self.head=Node(value)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(value)
    
    
    def delete(self,value):
        curr=self.head
        prev=None
        while curr:
            if curr.value==value:
                #value found in head node
                if curr==self.head:
                    self.head=curr.next
                    curr.next=None
                #value found in tail node
                elif curr.next==None:
                    prev.next=None
                #value found in a node that inside head and tail
                else:
                    prev.next=curr.next
                    curr.next=None
            prev=curr
            curr=curr.next
    
    
    def search(self,value):
        curr=self.head
        while curr:
            if curr.value==value:
                break
            curr=curr.next
        if curr:
            print('value found')
        else:
            print('Value is not found')
    
    def _searchRecursive(self,value,head):
        if head==None:
            return -1
        if head.value==value:
            return 1
        res=self._searchRecursive(value,head.next)
        if res==-1:
            return -1
        else:
            return 1


    def searchRecursive(self,value):
        head=self.head
        res=self._searchRecursive(value,head)
        return res


    def print(self):
        curr=self.head
        while curr:
            print(curr.value)
            curr=curr.next


