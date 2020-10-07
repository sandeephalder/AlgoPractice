
class BitonicSequence():

    sequence = [2,-1,4,3,5,-1,3,2]
    cal_states = [1 for i in range(len(sequence))] 
    cal_states_back = [1 for i in range(len(sequence))] 
    cal_states_final = []
    #

    def print(self):
    
        print('forward states -->',self.cal_states,end='-->\n\n')
        print('back states -->',self.cal_states_back,end='-->\n\n')
        print('final states -->',self.cal_states_final,end='-->\n\n')
                

    def compute(self):
        for i in range(1,len(self.sequence)):
            for j in range(i):
                if self.sequence[j] < self.sequence[i]:
                    if self.cal_states[j] +1 > self.cal_states[i]:
                        self.cal_states[i] = self.cal_states[j]+1
        self.sequence = self.sequence[::-1]
        for i in range(1,len(self.sequence)):
            for j in range(i):
                if self.sequence[j] < self.sequence[i]:
                    if self.cal_states_back[j] +1 > self.cal_states_back[i]:
                        self.cal_states_back[i] = self.cal_states_back[j]+1
        self.cal_states_back = self.cal_states_back[::-1]
        self.cal_states_final = [self.cal_states[i] + self.cal_states_back[i] -1 for i in range(len(self.sequence))]

            

                  
k = BitonicSequence()
k.compute()
k.print()
