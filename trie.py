'''
    Assumption: 1. Only Lowecase character
                2. No empty string as input
'''

class Node(object):
    def __init__(self,char):
        self.char= char
        self.isWord= False
        self.children={}

class Trie(object):
    
    def __init__(self):
        self.root= Node('\0')

    def insert(self,word):
        curr=self.root
        for char in word:
            if char in curr.children:
                curr=curr.children[char]
            else:
                curr.children[char]=Node(char)
                curr= curr.children[char]
        curr.isWord=True
        
    def _searchHelper(self,word):
        curr=self.root
        for char in word:
            if char in curr.children:
                curr=curr.children[char]
            else:
                return None
        return curr
    def search(self,word):
        node=self._searchHelper(word)
        return node!=None and node.isWord
    
    def startWithPrefix(self,word):
        node=self._searchHelper(word)
        if node is None:
            return []         
        self.output = []
        self._dfs(node, word[:-1])
 
        return self.output
    def _dfs(self, node, pre):
 
        if node.isWord:
            self.output.append((pre + node.char))
         
        for key in node.children:
            self._dfs(node.children[key], pre + node.char)
         
    def deleteWord(self,word):
        if word[0] in self.root.children:
            self._deleteWord(self.root.children[word[0]],word[1:],self.root)
    
    def _deleteWord(self,node, pre,prev):
        if not pre:
            if not node.children and node.isWord:
                del prev.children[node.char]
                return 
            else:
                return
        if pre[0] in node.children:
            self._deleteWord(node.children[pre[0]],pre[1:],node)
            if not node.children and not node.isWord:
                del prev.children[node.char]
        else:
            return
            
trie=Trie()
trie.insert("raid")
trie.insert("rear")
trie.insert("realy")
trie.insert("rain")
trie.startWithPrefix("rai")
trie.deleteWord("realy")
print(trie.search("rear"))
print(trie.search("realy"))
