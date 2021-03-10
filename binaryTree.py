class Treenode (object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinaryTree(object):
    def __init__(self,value=None):
        if not value:
            self.root=None
        else:
            self.root=Treenode(value)

    def insertRight(self,value):
        if self.root == None:
            self.root = BinaryTree(value)
        else:
            self._insertRight(self.root,value)
        
    def _insertRight(self,node,value):
        if node.rightChild==None:
            node.rightChild=Treenode(value)
        else:
            self._insertRight(node.rightChild,value)


    def insertLeft(self,value):
        if self.root == None:
            self.root = BinaryTree(value)
        else:
            self._insertLeft(self.root,value)
        
    def _insertLeft(self,node,value):
        if node.leftChild==None:
            node.leftChild=Treenode(value)
        else:
            self._insertLeft(node.rightChild,value)
    
    def _preorder(self, node):
        if node==None:
            return

        print(node.value)
        self._preorder(node.leftChild)
        self._preorder(node.rightChild)
 
    def preorder(self):
        self._preorder(self.root)

    def _postorder(self,node):
        if node==None:
            return
        self._postorder(node.leftChild)
        self._postorder(node.rightChild)
        print(node.value)

    def postorder(self):
        self._postorder(self.root)


    def _inorder(self,node):
        if node==None:
            return
        self._inorder(node.leftChild)
        print(node.value)
        self._inorder(node.rightChild)
        

    def inorder(self):
        self._inorder(self.root)

    def _bfs(self, node):
        if node==None:
            return
        q=[node]
        while len(q)!=0:
            n=q.pop(0)
            print(n.value)
            if n.leftChild!=None:
                q.append(n.leftChild)
            if n.rightChild!=None:
                q.append(n.rightChild)

    def bfs(self):
        self._bfs(self.root) 

def constructTreeHelper(arr, root, i, n):       
    if i < n: 
        temp = Treenode(arr[i])  
        root = temp
        root.leftChild = constructTreeHelper(arr, root.leftChild, 2 * i + 1, n)
        root.rightChild = constructTreeHelper(arr, root.rightChild, 2 * i + 2, n) 
    return root

def constructTree(arr):
    tree= BinaryTree()
    tree.root=constructTreeHelper(arr,tree.root,0,len(arr))
    return tree

tree=constructTree([5,4,6,7,8,3,9,0])
tree.preorder()