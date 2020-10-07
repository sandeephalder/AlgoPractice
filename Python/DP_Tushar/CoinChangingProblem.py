class CoinChanging():
    sum = 11
    coins = [1,5,6,8]
    knapsack = [[0 for i in range(11+1)] for j in range(len(coins)+1)]

    def print(self):
        for i in range(len(self.coins)):
            print()
            for j in range(11+1):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.coins)):
            for j in range(12):
                if i ==0:
                    print('j==',j)
                    if j >= self.coins[i]:
                        self.knapsack[i][j] = self.knapsack[i][j-1] +1

                else:
                    if j < self.coins[i]:
                        self.knapsack[i][j] = self.knapsack[i-1][j]
                    else:
                        self.knapsack[i][j] = min(self.knapsack[i-1][j],self.knapsack[i][j-self.coins[i]]+1) 





                        

 


                    
k = CoinChanging()
k.compute()
k.print()
