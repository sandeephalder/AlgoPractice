
class NumbersWithoutConsecutiveOnes():

    def print(self,val):
        print(self.compute(val))
        

    def compute(self,stair):
        if stair <= 0:
            return 1
        elif stair == 1:
            return 2
        else:
            return self.compute(stair-2) + self.compute(stair-1)

            
               
k = NumbersWithoutConsecutiveOnes()
k.print(4)
