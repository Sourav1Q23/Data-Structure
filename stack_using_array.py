class Stack:
    MAX_SIZE=10
    def __init__(self):
        self.stack=[]
        self.size = 0
    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size > 0 else False

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return "Stack is empty"
    
    def push(self,value):
        if self.getSize()==Stack.MAX_SIZE: 
            return "Stack is full "
        else: 
            self.stack.append(value)
            self.size+=1
    def pop(self):
        if self.getSize()==0:
            return "Stack is empty"
        else:
            self.size-=1
            return self.stack.pop()
        
        

        