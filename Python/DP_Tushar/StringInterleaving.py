class StringInterleaving():
    str1 = 'aab'
    str2 = 'axy'
    matcher_string = 'aaxaby'
    states = [[False for i in range(3+1)] for j in range(3+1)]

    def print(self):
        for i in range(len(self.str2)+1):
            print()
            for j in range(len(self.str1)+1):
                print('-->',self.states[i][j],end='-->')

    def compute(self):
        self.states[0][0] =True
        for i in range(1,len(self.str1)):
            if self.str1[i-1] == self.matcher_string[i-1]:
                self.states[0][i] = self.states[0][i-1]
            if self.str2[i-1] == self.matcher_string[i-1]:
                self.states[i][0] = self.states[i-1][0]
        
        for i in range(len(self.str1)+1):
            for j in range(len(self.str2)+1):  
                if i ==0 or j == 0:
                    continue
                else:
                    if self.str1[j-1] == self.matcher_string[i+j-1]:
                        self.states[i][j] = self.states[i][j-1]
                        print('1 i= ',i,' j=',j,self.states[i-1][j],self.matcher_string[i+j-1],self.str1[j-1])
                        continue
                    if self.str2[i-1] == self.matcher_string[j+i-1]:
                        self.states[i][j] = self.states[i-1][j]
                        print('2 i= ',i,' j=',j,self.states[i][j-1],self.matcher_string[j+i-1],self.str2[j-1])



k = StringInterleaving()
k.compute()
k.print()
