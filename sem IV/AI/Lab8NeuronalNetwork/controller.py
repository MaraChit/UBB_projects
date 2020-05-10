from neuronalNetwork import NeuronalNetwork
from repository import Repository
import matplotlib.pyplot as mpl
import numpy as np

class Controller:
    
    def __init__(self, repository : Repository):
        self.repository = repository

    def plotLoss(self, iterations,loss):
        '''
        plots graphic for the loss function
        '''
        mpl.plot(iterations, loss, label='loss value vs iteration')
        mpl.xlabel('Iterations')
        mpl.ylabel('loss function')
        mpl.legend()
        mpl.show()
        
    def runAlg(self):
        data = self.repository.data
        xL = []
        yL = []
        for elem in data:
            xL.append(elem[:-1])
            yL.append([elem[-1]])
        x = np.array(xL)
        y = np.array(yL)
        nn = NeuronalNetwork(x, y, 2)
        nn.loss = []
        iterations = []
        for i in range(1000):
            nn.feedforward()
            nn.backprop(0.00000001)
            iterations.append(i)
            
        print("Minimum loss is:")
        print(min(nn.loss))
        
        self.plotLoss(iterations, nn.loss)


