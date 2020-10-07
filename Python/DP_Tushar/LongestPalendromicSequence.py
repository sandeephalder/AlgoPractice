class LongestPalindromicSequence():
    str1 = 'agbdba'
    knapsack = [[0 for i in range(6)] for j in range(6)]

    def print(self):
        for i in range(len(self.str1)):
            print()
            for j in range(len(self.str1)):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.str1)+1):
            
            print()
            for j in range(len(self.str1)):
                if i+j >= len(self.str1):
                    continue
               

                
                if i==0:
                    self.knapsack[j][j]= 1
                elif self.str1[j] == self.str1[j+i]:
                    self.knapsack[j][i+j] = self.knapsack[j+1][i+j-1] +2
                else:
                    if i+j+1 <= len(self.str1):
                        self.knapsack[j][i+j] = max(self.knapsack[j][i+j-1] ,self.knapsack[j+1][i+j] )
                    else:
                        self.knapsack[j][i+j] = self.knapsack[j][i+j-1]


            
                    

               
            print()
            self.print()
            print()


               
                    
k = LongestPalindromicSequence()
k.compute()
k.print()
