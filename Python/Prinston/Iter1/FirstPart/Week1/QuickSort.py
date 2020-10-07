class QuickSort(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,4,1,6513,516,51,56,151,3]
        self.N = len(self.arr)
        self.print()
        self.sort(0,self.N-1)
        self.print()


    def print(self):
         print('==>',self.arr)

    def sort(self,start,end):
        if start >= end:
            return
        j= self.partition(start,end)
        self.sort(start,j-1)
        self.sort(j+1,end)


    def partition(self,start,end):
        j= start
        k= self.arr[start]
        l= end+1


        while True:
            while self.arr[j] <= k:
                j+=1
                if j>l:
                   break
                
            
            while True:
                l-=1
                if l< j or self.arr[l] < k:
                    break
      
            if l <= j:
                break

            self.exch(l,j)

        self.exch(start,l)
        return l
        
    def exch(self,src,dest):
        srcd= self.arr[src]
        self.arr[src] = self.arr[dest]
        self.arr[dest] = srcd

sort = QuickSort()
