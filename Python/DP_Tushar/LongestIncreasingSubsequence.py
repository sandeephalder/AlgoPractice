class LongestIncreasingSubsequence():
    sum = 11
    sequence = [3,4,-1,0,6,2,3]
    knapsack = [1 for i in range(len(sequence))] 

    def print(self):
        for i in range(len(self.sequence)):
            print('-->',self.knapsack[i],end='-->')
                

    def compute(self):
        for i in range(1,len(self.sequence)):
            for j in range(i):
                if self.sequence[j] < self.sequence[i]:
                    if self.knapsack[j] +1 > self.knapsack[i]:
                        self.knapsack[i] = self.knapsack[j]+1 

            

                  
k = LongestIncreasingSubsequence()
k.compute()
k.print()
