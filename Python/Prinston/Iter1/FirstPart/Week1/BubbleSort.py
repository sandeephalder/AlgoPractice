class BubbleSort(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,41,6513,516,51,56,151,3]
        self.N = len(self.arr)
        self.sort()


    def print(self):
         print('==>',self.arr)

    def sort(self):
        for i in range(0,self.N):
            for j in range(0,self.N):
                if self.arr[j] > self.arr[i]:
                    self.exch(i,j)   
    
    def exch(self,src,dest):
        srcd= self.arr[src]
        self.arr[src] = self.arr[dest]
        self.arr[dest] = srcd


sort = BubbleSort()
sort.print()