class MergeSort(object):

    def __init__(self):
        self.arr = [65,1,435,484,35,4,1,6513,516,51,56,151,3]
        self.aux = list(self.arr)
        self.N = len(self.arr)
        self.sort(0,self.N-1,self.arr)


    def print(self):
         print('==>',self.arr)

    def sort(self,start,end,array):
        if start>=end:
            return
        mid = int(int(end-start)/2)+start

        

        self.sort(start,mid,array)
        self.sort(mid+1,end,array)        
        self.merge(start,mid,end,array)



    def merge(self,start,mid,end,array):
        
        print('start={0},mid={1},end={2}'.format(start,mid,end))
        for i in range(start,end+1):
            self.aux[i]=self.arr[i]
            

        print('aux=',self.aux)

        i=start
        j=mid+1

        for k in range(start,end+1):
            print('i={0},j={1},k={2}'.format(i,j,k))
            if i > mid:
                self.arr[k]= self.aux[j]
                print('Case 1')
                j+=1
            elif j > end:
                self.arr[k]= self.aux[i]
                i+=1 
                print('Case 2')
            elif self.aux[i] > self.aux[j]:
                self.arr[k] = self.aux[i]
                i+=1
                print('Case 3')
            else:
                self.arr[k] = self.aux[j]
                j+=1
                print('Case 4')

            print('arr=',self.arr)

        
        


    def exch(self,src,dest):
        srcd= self.arr[src]
        self.arr[src] = self.arr[dest]
        self.arr[dest] = srcd


sort = MergeSort()
sort.print()