import numpy as np

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    def d_sigmoid(self,x):
        return x*(1-x)
