from random import random, randint

class Ant:
    def __init__(self, n):
        '''
        constructor
        '''
        self._n = n
        self.path = self.initPath()

    def initPath(self):
        '''
        generate a random matrix for the path
        '''
        l = []
        for i in range(self._n):
            l.append([])
            for j in range(self._n):
                l[i].append([randint(1,self._n), randint(1,self._n)])
        return l

    def evaluate(self):
        '''
        evaluates a path and returns the number of errors
        '''
        errors = 0
        for line in self.path:
            indS = [0] * self._n
            indT = [0] * self._n
            for [i,j] in line:
                if 0 < i < self._n:
                    indS[i - 1] = 1
                if 0 < j < self._n:
                    indT[j - 1] = 1
            for i in range(len(indS)):
                if indS[i] == 0:
                    errors = errors + 1
                if indT[i] == 0:
                    errors = errors + 1
        for i in range(self._n):
            indS = [0] * self._n
            indT = [0] * self._n
            for j in range(self._n):
                if 0< self.path[j][i][0] < self._n:
                    indS[self.path[j][i][0]-1] = 1
                if 0< self.path[j][i][1] < self._n:
                    indT[self.path[j][i][1] - 1] = 1
            for k in range(len(indS)):
                if indS[k] == 0:
                    errors = errors + 1
                if indT[k] == 0:
                    errors = errors + 1
        for i in range(self._n):
            for j in range(self._n):
                for k in range(self._n):
                    for l in range(self._n):
                        if i!=k or j!=l:
                            if self.path[i][j]==self.path[k][l]:
                                errors = errors+1
        return errors

    def update(self,q0, trace, alpha, beta):
        
        x = randint(0,self._n-1)
        y = randint(0,self._n-1)
        p = [[randint(1,self._n), randint(1,self._n)] for i in range(self._n)]
        p=[[int((p[i][0]**beta)*(trace[self.path[x][y][0]-1][self.path[x][y][0]-1][0]**alpha)),
            int((p[i][1]**beta)*(trace[self.path[x][y][0]-1][self.path[x][y][0]-1][0]**alpha))] for i in range(len(p))]
        if(random() < q0):
            r = [[i, p[i]] for i in range(len(p))]
            r = max(r, key=lambda a: a[1])

            self.path[x][y]=p[r[0]]
        else:
            r = randint(0,len(p)-1)
            self.path[x][y]=p[r]
