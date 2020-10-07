class CuttingRodmaxProfit():
    len=5 
    l = [1,2,3,4]
    profit = [2,5,7,8]
    knapsack = [[0 for i in range(6)] for j in range(4)]

    def print(self):
        for i in range(len(self.l)):
            print()
            for j in range(6):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.l)):
            print()
            for j in range(6):
                if j ==0:
                    continue
                elif i ==0:
                    if j%self.l[i] ==0:
                        self.knapsack[i][j] = int(j/self.l[i]*self.profit[i])
                else:
                    if j < self.l[i]:
                        self.knapsack[i][j] =  self.knapsack[i-1][j]
                    else:
                        self.knapsack[i][j] = max(self.knapsack[i-1][j],self.knapsack[i][j-self.l[i]] + self.profit[i])





                    
k = CuttingRodmaxProfit()
k.compute()
k.print()
