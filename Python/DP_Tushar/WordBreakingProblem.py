class WordBreakingInDictionary():
    string = 'iamace'
    dictionary=['i','a','am','ace']
    knapsack = [[False for i in range(6+1)] for j in range(6+1)]

    def print(self):
        for i in range(len(self.string)+1):
            print()
            for j in range(len(self.string)+1):
                print('-->',self.knapsack[i][j],end='-->')

    def compute(self):
        for i in range(len(self.string)+1):
            print()
            for j in range(len(self.string)+1):
                if i+j > len(self.string) or i==0:
                    continue
                elif i==1:
                    if self.string[i+j-1] in self.dictionary:
                        self.knapsack[j][i+j] = True
                        print('direct match -->',self.string[i+j-1])
                else:
                    self.knapsack[j][i+j] = self.calculateDictChar(i,j)

    def calculateDictChar(self,start,end):

        response = False

        if self.string[int(end):int(start+end)] in self.dictionary:
            print('True',self.string[int(end):int(start+end)])
            return True
        else:
            for i in range(start):
                if self.knapsack[end][end+i+1] and self.knapsack[end+i+1][start+end] or self.knapsack[end][end+i+1] and self.knapsack[end+i+1][start+end] is None:
                    print('True',self.string[int(end):int(start+end)])
                    return True
                print('False ','start= ',start,' end= ',end,' first = ',self.string[end:end+i+1],' second = ',self.string[end+i+1:start+end],' first_match= ',self.knapsack[end][end+i+1],' second_match= ',self.knapsack[end+i+1][start+end])
            return response   



k = WordBreakingInDictionary()
k.compute()
k.print()
