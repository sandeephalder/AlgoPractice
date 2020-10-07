import math
class MinimumJumpsToReachEnd():
    weights = [2,3,1,1,2,4,2,0,1,1]
    N = len(weights)
    jumps= [math.inf]*N
    sources =[i for i in range(N)]
    

    def print(self):
        print('Jumps:   ',self.jumps)
        print('Sources: ',self.sources)


    def compute(self):
        self.jumps[0]=0
        for i in range(self.N):
            for j in range(i):
                if self.weights[j] >= i-j and self.jumps[j] +1 < self.jumps[i] :
                    self.jumps[i]= self.jumps[j] +1
                    self.sources[i] =j
                    


                    
k = MinimumJumpsToReachEnd()
k.compute()
k.print()
