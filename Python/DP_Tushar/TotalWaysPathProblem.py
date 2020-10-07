
class TotalWaysPathProblem():
   metrics = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
   states=[[1 for i in range(4)] for j in range(4)]



   def print(self):
        for i in range(4):
            print()
            for j in range(4):
                print('-->',self.states[i][j],end='-->')

   def compute(self):
        for i in range(4):
            print()
            for j in range(4):
                if i ==0 or j ==0:
                    continue
                else:
                    self.states[i][j] = self.states[i-1][j] + self.states[i][j-1]

                    
k = TotalWaysPathProblem()
k.compute()
k.print()
