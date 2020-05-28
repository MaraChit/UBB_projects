from fuzzyVariable import FuzzyVariable
import numpy as np

class Capacity(FuzzyVariable):
    
    def __init__(self, value):
        
        self.value = value
        #using fig 8
        self.labels = {
            'small': [(-np.inf, 1), (1, 1), (2, 0), (np.inf, 0)],
            'medium': [(-np.inf, 0), (1, 0), (2.5, 0), (4, 0), (np.inf, 0)],
            'high': [(-np.inf, 0), (3, 0), (4, 1), (np.inf, 1)]
        }