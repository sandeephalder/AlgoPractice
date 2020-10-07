class BuySellStockKTransactions():
    k=3
    price = [2,5,7,1,4,3,1,3]
    transactions = [[0 for i in range(8)] for j in range(k+1)]

    def print(self):
        for i in range(self.k+1):
            print()
            for j in range(len(self.price)):
                print('-->',self.transactions[i][j],end='-->')

    def compute(self):
        for i in range(self.k+1):
            print()
            for j in range(len(self.price)):
                if i==0 or j==0:
                    continue
                else:
                    self.transactions[i][j] = self.calculatePrice(i,j)

    def calculatePrice(self,i,j):
        max_vals= [self.transactions[i][j-1]]
        for k in range(j):
            max_vals.append(self.transactions[i-1][k]+ self.price[j] - self.price[k])
        print('i= ',i,' j= ',j,' max_vals= ',max_vals)
        return max(max_vals)

                    
k = BuySellStockKTransactions()
k.compute()
k.print()
