class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None    

class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        currentNode=self.root
        if currentNode:
            while True:
                if value < currentNode.value :
                    if currentNode.left is None:
                        currentNode.left=Node(value)
                        break
                    else:
                        currentNode = currentNode.left
                else:    
                    if currentNode.right is None:
                        currentNode.right=Node(value)
                        break
                    else:
                        currentNode = currentNode.right
        
        else:
            self.root=Node(value)
        
    def search(self,value):
        currentNode=self.root
        while currentNode is not None:
            if value < currentNode.value:
                currentNode=currentNode.left
            elif value > currentNode.value:
                currentNode=currentNode.right
            else:
                return True
        return False

    def remove(self, value , root=None , parentNode=None):
        currentNode=self.root if root==None else root
        while currentNode is not None:

            if value < currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.left

            elif value > currentNode.value:
                parentNode=currentNode
                currentNode=currentNode.right
            
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value=self.getMinValue(currentNode.right)
                    self.remove(currentNode.value,currentNode.right,currentNode)
                
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value=currentNode.left.value
                        currentNode.left=currentNode.left.left
                        currentNode.right=currentNode.left.right
                    elif currentNode.right is not None:
                        currentNode.value=currentNode.right.value
                        currentNode.left=currentNode.right.left
                        currentNode.right=currentNode.right.right                    
                    else:
                        currentNode=None

                elif parentNode.left==currentNode:
                    parentNode.left=currentNode.left if currentNode.left is not None else currentNode.right 

                elif parentNode.right==currentNode:                    
                    parentNode.right=currentNode.left if currentNode.left is not None else currentNode.right
                break

    def getMinValue(self,currentNode):
        while currentNode.right is not None:
            currentNode=currentNode.right
        return currentNode.value   

bst=BST()
bst.insert(5)            
bst.insert(7)            
bst.insert(9)            
bst.insert(4)            
bst.insert(1)            
bst.insert(-7)            
bst.insert(8)            
bst.insert(10)            
bst.insert(3)            

