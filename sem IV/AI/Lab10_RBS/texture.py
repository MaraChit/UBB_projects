from fuzzyVariable import FuzzyVariable
import numpy as np

class Texture(FuzzyVariable):
    
    def __init__(self, value):
        
        self.value = value
        #using fig 7
        self.labels = {
            'very_soft': [(-np.inf, 1), (0.2, 1), (0.4, 0), (np.inf, 0)],
            'soft': [(-np.inf, 0), (0.2, 0), (0.4, 1), (0.8, 0), (np.inf, 0)],
            'normal': [(-np.inf, 0), (0.3, 0), (0.7, 1), (0.9, 0), (np.inf, 0)],
            'resistant': [(-np.inf, 0), (0.7, 0), (0.9, 1), (np.inf, 1)]
        }
