class DSU(object):
    def __init__(self,n,arr):
        self.arr=arr
        self.parent=[None]*n
        self.size=[0]*n

    def find_set(self,v):    #Find Parent of given value
        i=self.arr.index(v)
        if v == self.parent[i]:
            return v
        self.parent[i] = self.find_set(self.parent[i]) #path compression 
        return self.parent[i]

    def make_set(self,i,v): # Init the set
        self.parent[i] = v
        self.size[i] = 1

    def union_sets(self,a,b):  #Union Between two value
        a = self.find_set(a) # Find the parent of a
        b = self.find_set(b) # Find the parent of b  
        i=self.arr.index(a)
        j=self.arr.index(b)
        if a == b: 
            return
    

        if self.size[i] < self.size[j]: #Joining set using size of two set
            self.parent[i] = b 
            self.size[i]+=self.size[j]
    
        else: 
            self.parent[j] = a
            self.size[j]+=self.size[i]

