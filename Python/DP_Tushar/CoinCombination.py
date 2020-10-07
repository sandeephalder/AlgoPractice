
class CoinCombination():
    sum = 5
    coins = [1,2,3]
    total = [[0 for i in range(5+1)] for j in range(3)]
    

    def print(self):
        print()
        for i in range(len(self.coins)):
            print()
            for j in range(5+1):
                print('==>',self.total[i][j],end='   ')
     
    def compute(self):
       for i in range(len(self.coins)):
            for j in range(5+1):
                if i == 0:
                    self.total[i][j] = 1
                elif j < self.coins[i]:
                    self.total[i][j] = self.total[i-1][j]
                else:
                    self.total[i][j] = max(self.total[i-1][j],self.total[i][j-self.coins[i]]+self.total[i-1][j])
               
k = CoinCombination()
k.compute()
k.print()
