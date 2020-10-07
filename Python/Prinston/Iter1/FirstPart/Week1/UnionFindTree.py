class UnioFindTree(object):
    
    def __init__(self):
        self.arr = list(range(0,10))
      
    def print(self):
        print("\nUnion Find:",self.arr)

    def connect(self,src,dest):
        self.srcd= self.root(self.arr[src])
        self.destd= self.root(self.arr[dest])
        self.arr[self.srcd]= self.destd
        

    def isConnected(self,src,dest):
        return self.root(self.arr[src])==self.root(self.arr[dest])

    def root(self,src):
        while(self.arr[src]!=src):
            src=self.arr[src]
        return src    



uf = UnioFindTree()
uf.connect(0,1)
uf.connect(0,2)
uf.connect(0,5)
uf.connect(0,7)
uf.connect(0,9)
print("isConnected",uf.isConnected(1,9))
print("isConnected",uf.isConnected(1,6))