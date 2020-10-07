class MinimumEditDistance():
    str1 = 'abcdef'
    str2 = 'azced'
    knapsack = [[0 for i in range(6+1)] for j in range(5+1)]

    def print(self):
        for i in range(len(self.str2)+1):
            print()
            for j in range(len(self.str1)+1):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.str2)+1):
            for j in range(len(self.str1)+1):
                if i ==0:
                    self.knapsack[i][j] = j
                elif j ==0:
                    self.knapsack[i][j] =i
                else:
                    if self.str2[i-1] == self.str1[j-1]:
                        self.knapsack[i][j] = self.knapsack[i-1][j-1]
                    else:
                        self.knapsack[i][j] = min(self.knapsack[i-1][j],self.knapsack[i][j-1],self.knapsack[i-1][j-1]) +1
                
                    
k = MinimumEditDistance()
k.compute()
k.print()
