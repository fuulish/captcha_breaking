
import numpy as np
from mlc.perceptron import Perceptron

class Adaline(Perceptron):
    """
    Adaline (adaptive linear neuron) classifier

    Attributes
    ----------
    errors_ : list
        number of misclassification in each pass (epoch)
    w_ : 1d-array
        weights after optimization
    theta_ : float
        threshold for classification
    """

    def __init__(self, *args, **kwargs):
        super(Adaline, self).__init__(*args, **kwargs)

        self.cost_ = []

    def activation(self, X):
        return self.net_input(X)

    def fit(self, X, y):

        if self.standardize:
            X = self.standardize_data(X)

        self.theta_ = 0
        self.w_ = np.zeros(X.shape[1])
        self.errors_ = []

        for _ in range(self.niter):
            errors = (y - self.net_input(X))
            # print errors, X.T.dot(errors)
            print self.w_

            self.w_ += self.eta * X.T.dot(errors) #np.dot(X, errors)
            self.theta_ += self.eta * errors.sum()

            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)

        return self

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)


    #def net_input(self, X):
    #    return np.dot(X, self.w_) + self.theta_
