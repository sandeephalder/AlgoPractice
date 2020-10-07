class Stack(object):
   
    

    def __init__(self):
        
        self.TOP = 0
        self.N= 10
        self.arr = [None]*self.N
        
        for i in range(0,self.N-1):
            self.arr[i]=i

    def push(self,val):
        if self.TOP >  self.N:
            raise Exception('Stack is full')
        self.arr[self.TOP+1]=val
        self.TOP += 1

    def pop(self):
        if self.TOP <= 0:
            return "Stack is empty"
        val = self.arr[self.TOP]
        self.TOP -=1
        return val

    def print(self):
        print('arr',self.arr)


stack = Stack()
stack.push(1)
stack.push(4)
stack.push(1)
stack.push(4)
stack.push(13)
stack.push(1)
stack.push(4)
stack.push(13)
stack.push(1)
stack.push(4)
stack.push(13)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())