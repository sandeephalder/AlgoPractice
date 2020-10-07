class KnapSack():
    W=8
    v = [1,4,5,7]
    w= [1,3,4,5]
    knapsack = [[0 for i in range(8)] for j in range(len(v))]

    def print(self):
        for i in range(len(self.w)):
            print()
            for j in range(self.W):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.w)):
            for j in range(self.W):
                if i == 0:
                    if j >= self.w[i]:
                         self.knapsack[i][j] = self.v[i]
                else:
                    if j >= self.w[i]:
                        knap = max(self.knapsack[i-1][j], self.knapsack[i-1][j-self.w[i]] + self.v[i])
                        self.knapsack[i][j] = knap
                    else:
                        self.knapsack[i][j] = self.knapsack[i-1][j]

                    
k = KnapSack()
k.compute()
k.print()
