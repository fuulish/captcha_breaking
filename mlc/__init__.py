from __future__ import print_function

__all__ = ['perceptron', 'adaline']

class MLC(object):
    """
    machine learning classifier

    Parameters
    ----------
    eta : float
        damping for optimization
    niter : int
        maximal number of iterations
    standardize : bool
        whether to standardize data (inplace)

    """
    def __init__(self, eta=0.01, niter=10, standardize=False):

        self.eta = eta
        self.niter = niter
        self.standardize = standardize

    def predict(self, X):
        """
        Predict target for input of feature vector

        Parameters
        ----------
        X : 1d-array
            feature vector

        Returns
        -------
        classification of input
        """

        print('child class needs to provide predict method')
        pass

    def fit(self, X, y):
        """
        optimize MLC for given set of input samples and known targets

        Parameters
        ----------
        X : 2d-array (nsamples, nfeatures)
            feature array for nsamples data points
        y : 1d-array (nfeatures)
            target values for input features

        Returns
        -------
        self : object
        """

        print('child class needs to provide fit method')
        pass

    def standardize_data(self, X):
        """
        standardize input data (feature vectors)

        Parameters
        ----------
        X : 2d-array (nsamples, nfeatures)
            feature array for nsamples data points

        Returns
        -------
        X : 2d-array (nsamples, nfeatures)
            rescaled and recentered feature array for nsamples data points
        """

        return (X - X.mean(axis=0)) / X.std(axis=0)
