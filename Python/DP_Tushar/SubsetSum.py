class SubsetSum():
    sum = 11
    numbers = [2,3,7,8,10]
    knapsack = [[False for i in range(11+1)] for j in range(len(numbers)+1)]

    def print(self):
        for i in range(len(self.numbers)):
            print()
            for j in range(11+1):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.numbers)):
            for j in range(12):
                if j ==0:
                    self.knapsack[i][j] = True
                elif i ==0:
                    if j == self.numbers[i]:
                        self.knapsack[i][j] = True
                    else:
                        self.knapsack[i][j] = False
                else:
                    if j == self.numbers[i]:
                        self.knapsack[i][j] = True
                    elif j< self.numbers[i]:
                        self.knapsack[i][j] = self.knapsack[i-1][j]
                    else:
                        self.knapsack[i][j] = self.knapsack[i-1][j-self.numbers[i]] | self.knapsack[i-1][j]


                    
k = SubsetSum()
k.compute()
k.print()
