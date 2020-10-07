class JobScheduling():
    jobs = [[1,3],[2,5],[4,6],[6,7],[5,8],[7,9]]
    rewards = [5,6,5,4,11,2]
    calculate = [i for i in rewards]

    def print(self):   
        print(self.calculate)
        
    def compute(self):
        for i in range(len(self.rewards)):
            print()
            for j in range(0,i):
                if self.jobs[j][1] <= self.jobs[i][0] and self.calculate[j] + self.rewards[i] >  self.calculate[i]: 
                    self.calculate[i] = self.calculate[j] + self.rewards[i]
            self.print()


                    
k = JobScheduling()
k.compute()
k.print()
