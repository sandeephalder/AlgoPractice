
class MaxSubsqueareWithSidesX():
   metrics = [[0,0,0,0,1],[1,0,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[0,0,1,1,1]]
   states=[[[0,0] for i in range(5)] for j in range(5)]



   def print(self):
        for i in range(5):
            print()
            for j in range(5):
                print('-->',self.states[i][j],end='-->')

   def compute(self):
       for i in range(5):
            print()
            for j in range(5):
                if i ==0:
                    if self.metrics[i][j] == 1:
                        self.states[i][j] = [1,1]
                elif j ==0:
                    if self.metrics[i][j] == 1:
                        self.states[i][j][0] = self.states[i-1][j][0] +1
                        self.states[i][j][1] = 1
                else:
                    if self.metrics[i][j] == 1:
                        self.states[i][j][0] = self.states[i-1][j][0] +1
                        self.states[i][j][1] = self.states[i][j-1][1] +1

                    
k = MaxSubsqueareWithSidesX()
k.compute()
k.print()
