class RegexMatch():
    pattern = 'xa*b.c'
    string = 'xaabyc'
    knapsack = [[False for i in range(6+1)] for j in range(6+1)]

    def print(self):
        for i in range(len(self.string)+1):
            print()
            for j in range(len(self.pattern)+1):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.string)+1):
            for j in range(len(self.pattern)+1):
                print()
                #print('i= ',i,' j=',j)
                print()
                #self.print()
                if i==0 and j ==0:
                    self.knapsack[i][j] =True
                elif i ==0 or j == 0:
                    self.knapsack[i][j] =False
                else:
                    if self.pattern[j-1] == '.' or self.pattern[j-1] == self.string[i-1]:
                        self.knapsack[i][j] = self.knapsack[i-1][j-1]
                    elif self.pattern[j-1] == '*':
                        if self.knapsack[i][j-2] == True:
                            self.knapsack[i][j] = True
                        elif self.knapsack[i-1][j] == True and self.pattern[j-2] == self.string[i-1]:
                            self.knapsack[i][j] = True
                    



                    
k = RegexMatch()
k.compute()
k.print()
