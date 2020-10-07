class BuySellStockKTransactions():
    line=10
    words = ['tushar','roy','likes','to','code']
    transactions = [[0 for i in range(5)] for j in range(5)]

    def print(self):
        for i in range(len(self.words)):
            print()
            for j in range(len(self.words)):
                print('-->',self.transactions[i][j],end='-->')

    def compute(self):
        pass

                    
k = BuySellStockKTransactions()
k.compute()
k.print()
