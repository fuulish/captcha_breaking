import numpy as np

from mlc import MLC

class Perceptron(MLC):
    """
    Perceptron classifier

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
        super(Perceptron, self).__init__(*args, **kwargs)
        # super.__init__(*args, **kwargs)

    def fit(self, X, y):

        if self.standardize:
            self.standardize_data(X)

        self.theta_ = 0
        self.w_ = np.zeros(X.shape[1])
        self.errors_ = []

        for _ in range(self.niter):
            errors = 0
            for Xi, target in zip(X, y):
                step = self.eta * (target - self.predict(Xi))
                self.w_[:] += step * Xi
                self.theta_ += step

                errors += int(step != 0.0)

            self.errors_.append(errors)

    def predict(self, X):
        return np.where(self.net_input(X) > 0, 1, -1)

    def net_input(self, X):
        """
        Parameters
        ----------
        X : 1d-array
            feature array (for one sample)
        Returns
        -------
        float
            net input, i.e., sum over weights x features
        """

        return np.dot(self.w_, X) + self.theta_
