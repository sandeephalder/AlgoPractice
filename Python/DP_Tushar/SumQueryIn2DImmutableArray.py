class SumQueryIn2DImmutableArray():
   metrics = [[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]]
   states=[[1 for i in range(5)] for j in range(5)]



   def print(self):
        for i in range(5):
            print()
            for j in range(5):
                print('-->',self.states[i][j],end='-->')

   def compute(self):
       for i in range(5):
            print()
            for j in range(5): 
                if i==0 or j==0 :
                    self.states[i][j]= 0
                else:
                    self.states[i][j] = self.metrics[i-1][j-1] + self.states[i-1][j] + self.states[i][j-1] - self.states[i-1][j-1]

                    
k = SumQueryIn2DImmutableArray()
k.compute()
k.print()
