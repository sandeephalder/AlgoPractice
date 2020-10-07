class MergeSortBottomUp(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,4,1,6513,516,51,56,151,3]
        self.aux = list(self.arr)
        self.N = len(self.arr)
        self.sort(0,self.N-1)


    def print(self):
         print('==>',self.arr)

    def sort(self,start,end):
        if start>=end:
            return

#        for sz in range(1,self.N,2*sz):
#            for i in range(1,self.N,2*sz):
#                print('sz=',sz,'i=',i)

        sz=1
        while sz < self.N:
            i=0
            while i < self.N:
                print('sz=',sz,'i=',i)
                self.merge()
                i+=sz
            sz=2*sz


    def merge(self,start,mid,end):
        for i in range(start,end+1):
            self.aux[i]=self.arr[i]

        j = start
        k = mid+1

        for i in range(start,end+1):
            if j > mid :
                self.arr[i] = self.aux[k]
                k+=1
            elif k > end:
                self.arr[i] = self.aux[j]
                j+=1
            elif self.aux[j]>self.aux[k]:
                self.arr[i] = self.aux[j]
                j+=1
            else:
                self.arr[i] = self.aux[k]
                k+=1




sort = MergeSortBottomUp()

