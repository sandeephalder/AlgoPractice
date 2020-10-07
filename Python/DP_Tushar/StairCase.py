class StairCase():

    def print(self,val):
        print(self.compute(val))
        

    def compute(self,stair):
        if stair < 2:
            return 1
        else:
            return self.compute(stair-2) + self.compute(stair-1)

            
        


                    
k = StairCase()
k.print(4)
