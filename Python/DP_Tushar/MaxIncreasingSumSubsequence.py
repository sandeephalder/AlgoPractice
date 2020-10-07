class MaxIncreasingSumSubsequence():
    sum = 11
    sequence = [7,6,5,4,3,2,1]
    maxvalue = [i for i in sequence] 
    maxvaluefrom = [0 for i in range(len(sequence))] 

    def print(self):   
        
        print('maxvalue-->',self.maxvalue,end='-->\n')
    
        print('nmaxvaluefrom-->',self.maxvaluefrom,end='-->\n')
            

    def compute(self):
        for i in range(len(self.sequence)):
            for j in range(i):
                if self.sequence[i] > self.sequence[j]:
                    if self.maxvalue[i] < self.maxvalue[j] + self.sequence[i]:
                        self.maxvalue[i] = self.maxvalue[j] + self.sequence[i]
                        self.maxvaluefrom[i] =j
                print('i= ',i,' j= ',j,self.maxvalue)
            

                  
k = MaxIncreasingSumSubsequence()
k.compute()
k.print()
