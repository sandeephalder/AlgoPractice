class MinimumCostPath():
    weights = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]
    knapsack = [[0 for i in range(4)] for j in range(3)]

    def print(self):
        for i in range(3):
            print()
            for j in range(4):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        self.knapsack[0][0] = self.weights[0][0]
        for i in range(1,4):
            self.knapsack[0][i] = self.weights[0][i] +self.knapsack[0][i-1] 
        for i in range(0,3):
            self.knapsack[i][0] = self.weights[i][0] +self.knapsack[i-1][0]
        for i in range(3):
            for j in range(4):
                if i ==0 or j ==0:
                    continue
                else:
                    self.knapsack[i][j] = min(self.knapsack[i][j-1],self.knapsack[i-1][j]) + self.weights[i][j]
                     

                    
k = MinimumCostPath()
k.compute()
k.print()


