class Problem:
    def __init__(self):
        '''
        constructor
        '''
        self.n = None
        self.noEpoch = None
        self.noAnts = None
        self.alpha = None
        self.beta = None
        self.rho = None
        self.q0 = None


    def loadProblem(self):
        '''
        read data from file
        '''
        f = open("input.txt", "r")
        self.n = int(f.readline())
        self.noEpoch = int(f.readline())
        self.noAnts = int(f.readline())
        self.alpha = float(f.readline())
        self.beta = float(f.readline())
        self.rho = float(f.readline())
        self.q0 = float(f.readline())