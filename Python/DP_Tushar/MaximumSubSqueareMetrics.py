class MaximumSubSqueareMetrics():
    metrics = [[0,0,1,1,1],[1,0,1,1,1],[0,1,1,1,1],[1,0,1,1,1],]
    transactions = [[0 for i in range(5+1)] for j in range(4+1)]

    def print(self):
        for i in range(5):
            print()
            for j in range(6):
                print('-->',self.transactions[i][j],end='-->')

    def compute(self):
        for i in range(5):
            for j in range(6):
                if i==0 or j ==0:
                    continue
                else:
                    if self.metrics[i-1][j-1] ==1 :
                        self.transactions[i][j] = min(self.transactions[i-1][j],self.transactions[i][j-1],self.transactions[i-1][j-1]) +1


                    
k = MaximumSubSqueareMetrics()
k.compute()
k.print()
