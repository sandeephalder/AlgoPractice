class MaxSumNonAdjacent():
    sum = 11
    sequence = [4,1,1,4,2,1]
    inclusive=sequence[0]
    exclusive = 0 
    

    def print(self):   
        
        print(' inclusive--> ',self.inclusive,' exclusive--> ',self.exclusive,end='-->\n')
    
       
            

    def compute(self):
        for i in range(1,len(self.sequence)):
            old = self.inclusive
            self.inclusive = max(self.inclusive,self.exclusive + self.sequence[i])
            self.exclusive = old
            self.print()


           
            

                  
k = MaxSumNonAdjacent()
k.compute()
