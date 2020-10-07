class InsertionSort(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,4,1,6513,516,51,56,151,3]
        self.N = len(self.arr)
        self.sort()


    def print(self):
         print('==>',self.arr)

    def sort(self):
        for i in range(0,self.N):
            for j in range(i-1,-1,-1):
                if self.arr[j+1] < self.arr[j]:
                    self.exch(j+1,j)   
    
    def exch(self,src,dest):
        srcd= self.arr[src]
        self.arr[src] = self.arr[dest]
        self.arr[dest] = srcd


sort = InsertionSort()
sort.print()
