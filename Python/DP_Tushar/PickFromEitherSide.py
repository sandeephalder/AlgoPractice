class BuySellStockKTransactions():
    words = [3,9,1,2]
    transactions = [[[0,0] for i in range(5)] for j in range(5)]

    def print(self):
        for i in range(len(self.words)):
            print()
            for j in range(len(self.words)):
                print('-->',self.transactions[i][j],end='-->')

    def compute(self):
        for i in range(len(self.words)):
            print()
            for j in range(len(self.words)):
                if i+j >= len(self.words):
                    continue
                elif j==j+i:
                    self.transactions[j][j+i] = [self.words[j],0]
                else:
                    self.transactions[j][i+j] = self.calculate(i,j)

    def calculate(self,start,end):
        print(' start1= ',end,' end1= ' ,start+end-1) 
        print(' start2= ',end+1,' end2= ' ,start+end)
        first = self.transactions[end][start+end-1][1] + self.words[end+start] # 0,0
        second = self.transactions[end+1][start+end][1] + self.words[end] # 1,1
        
        if first > second:
            print('First: ', [first,self.transactions[end][start+end-1][0]],end='\n\n')
            return [first,self.transactions[end][start+end-1][0]]
        else:
            print('Second: ', [first,self.transactions[end][start+end-1][0]],end='\n\n')
            return [second,self.transactions[end+1][start+end][0]]
        return [-1,-1]


                    
k = BuySellStockKTransactions()
k.compute()
k.print()
