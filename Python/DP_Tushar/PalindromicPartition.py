import math
class PalindromePartition():
    string = 'abmcabac'
    calculate = [[0 for i in range(8+1)] for j in range(8+1)]

    def print(self):
        for i in range(len(self.string)):
            print()
            for j in range(len(self.string)):
                print('-->',self.calculate[i][j],end='-->')

    def compute(self):
        for i in range(len(self.string)):
            for j in range(len(self.string)):
                if j==i+j or i+j >= len(self.string):
                    continue
                else:
                    self.calculate[j][i+j] = self.calculatePalindrome(i,j)
                    
    
    def calculatePalindrome(self,start,end):
        print('start= ',end,' end= ',end+start , start,end)
        minimum = math.inf
        if self.isPalindrome(self.string[end:start+end+1]):
            minimum=0
        elif start==1:
            print('minimum is 1')
            minimum = 1
        else:
            for i in range(start):
                print('start_1: ',end,' end_1: ',i+end,' start_2: ',i+end+1,' end_2: ',start+end,' i=',i)

                m = self.calculate[end][i+end] + self.calculate[i+end+1][start+end] +1
                if minimum > m:
                    minimum= m 
        print(end='\n\n')
        return minimum


    def isPalindrome(self,string):
        for i in range(int(len(string)/2)):
            if string[i] != string[-i-1]:
                return False
        #print(string,' is Palindrome')
        return True

                

                    
k = PalindromePartition()
k.compute()
k.print()
