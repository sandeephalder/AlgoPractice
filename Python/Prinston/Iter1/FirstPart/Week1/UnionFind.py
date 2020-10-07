class UnioFind(object):
    
    def __init__(self):
        self.arr = list(range(0,10))
      
    def print(self):
        print("\nUnion Find:",self.arr)

    def connect(self,src,dest):
        srcd= self.arr[src]
        for i in range(0,10):
            if self.arr[i]==self.arr[dest]:
                self.arr[i]=srcd

    def isConnected(self,src,dest):
        return self.arr[src]==self.arr[dest]

uf = UnioFind()
uf.connect(0,1)
uf.connect(0,2)
uf.connect(0,5)
uf.connect(0,7)
uf.connect(0,9)
print("isConnected",uf.isConnected(1,9))
print("isConnected",uf.isConnected(1,6))