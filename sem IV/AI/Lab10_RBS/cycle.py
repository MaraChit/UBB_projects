from fuzzyVariable import FuzzyVariable
import numpy as np

class Cycle(FuzzyVariable):
    
    def __init__(self, value):
        self.value = value
        #using fig. 9
        self.labels = {
            'delicate': [(-np.inf, 1), (0.2, 1), (0.4, 0), (np.inf, 0)],
            'easy': [(-np.inf, 0), (0.2, 0), (0.5, 1), (0.8, 0), (np.inf, 0)],
            'normal': [(-np.inf, 0), (0.3, 0), (0.6, 1), (0.9, 1), (np.inf, 1)],
            'intense': [(-np.inf, 0), (0.7, 0), (0.9, 1), (np.inf, 1)]
        }