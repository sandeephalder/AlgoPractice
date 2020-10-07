import math

class CoinChangingBottomUp():
    sum = 13
    coins = [7,2,3,6]
    total = [math.inf for i in range(13+1)]
    freq = [-1 for i in range(13+1)]

    def print(self):
        print()
        for i in range(self.sum+1):
            print('({0}) ===>'.format(i),self.total[i],end='   ')
        print()
        for j in range(self.sum+1):
            print('({0}) ===>'.format(j),self.freq[j],end='   ')

    def compute(self):
        self.total[0]=0
        for i in range(len(self.coins)):
            for j in range(self.sum+1):
                if j >= self.coins[i] :
                    if self.total[j] > self.total[j-self.coins[i]] +1:
                        self.total[j] = min(self.total[j-self.coins[i]] +1,self.total[j]) 
                        self.freq[j] = i

            print()
            self.print()
            print()
               
k = CoinChangingBottomUp()
k.compute()
k.print()
