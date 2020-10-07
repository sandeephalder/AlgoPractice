class SelectionSort(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,4,1,6513,516,51,56,151,3]
        self.N = len(self.arr)
        self.sort()


    def print(self):
         print('==>',self.arr)

    def sort(self):
        for i in range(0,self.N):
            min = i
            for j in range(i,self.N):
                if self.arr[j] < self.arr[min]:
                    min=j
                self.exch(i,min)   
    
    def exch(self,src,dest):
        srcd= self.arr[src]
        self.arr[src] = self.arr[dest]
        self.arr[dest] = srcd


sort = SelectionSort()
sort.print()