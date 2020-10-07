
class EggDroppingproblem():
    floor = 6
    eggs = [1,2,3]
    total = [[0 for i in range(6+1)] for j in range(len(eggs)+1)]
    

    def print(self):
        print()
        for i in range(len(self.eggs)+1):
            print()
            for j in range(self.floor+1):
                print('==>',self.total[i][j],end='   ')
     
    def compute(self):
       for i in range(len(self.eggs)+1):
           for j in range(self.floor+1):
               if i == 0 or j ==0 :
                   continue
               elif i==1 :
                    self.total[i][j] = j
               elif j<i:
                   self.total[i][j] = self.total[i-1][j]  
               else:
                   self.total[i][j] = self.calculateMax(i,j)

    def calculateMax(self,egg,floor):
        max_result =[]
        print('egg= ',egg,' floor= ',floor)
        for curr_floor in range(1,floor+1):
            max_val = max(self.total[egg-1][curr_floor-1],self.total[egg][floor-curr_floor]) +1
            max_result.append(max_val)
            print('egg= ',egg,' floor= ',floor,' curr_floor= ',curr_floor,' max1= ',self.total[egg-1][curr_floor-1],' max2= ',self.total[egg][floor-curr_floor],' max_val= ',max_val)
        return min(max_result) 



k = EggDroppingproblem()
k.compute()
k.print()