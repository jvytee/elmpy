"""Basic Extreme Learning Machine implemented in pure NumPy"""

import numpy as np


class ELMRegressor():
    """Simple implementation of an Extreme Learning Machine for regression learning

    Parameters
    ----------
    n_hidden : int
        Number of hidden nodes, defaults to 50
    alpha : float
        Alpha value for sigmoidal activation function:
        f(x) = 1 / (1 + exp(-αx))
    gamma : float
        Regularization strength for regularized ELM implementation
    """

    def __init__(self, n_hidden: int = 50, alpha: float = 1.0, gamma: float = None):
        self.n_hidden = n_hidden
        self.alpha = alpha
        self.gamma = gamma

        self.w_in = None
        self.w_out = None
        self.bias = None

    def __forward(self, x: np.ndarray, w: np.ndarray, b: np.ndarray = None) -> np.ndarray:
        """Helper method to estimate forward pass through one network layer, including activation function

        Parameters
        ----------
        x : np.ndarray
            Matrix of input vectors
        w : np.ndarray
            Weight matrix
        b : np.ndarray
            Bias vector. Will set to all zeros if None

        Returns
        -------
        np.ndarray
            Matrix of output vectors
        """
        bias = np.zeros(w.shape[0]) if b is None else b
        v = np.dot(w, x.T).T + bias
        return 1 / (1 + np.exp(-self.alpha * v))

    def fit(self, xs: np.ndarray, ys: np.ndarray) -> None:
        """Train ELM by applying ridge regression to output weights

        Parameters
        ----------
        xs : np.ndarray
            Sample input values
        ys : np.ndarray
            Sample output values
        """
        if self.w_in is None:
            # self.w_in = np.random.rand(self.n_hidden, xs[0].shape[0])
            self.w_in = np.random.rand(self.n_hidden, xs.shape[1]) * 2 - 1

        if self.bias is None:
            # self.bias = np.random.rand(self.n_hidden)
            self.bias = np.random.rand(self.n_hidden) * 2 - 1

        hidden = self.__forward(xs, self.w_in, self.bias)

        if self.gamma is None:
            self.w_out = np.matmul(np.linalg.pinv(hidden), ys)
        else:
            self.w_out = np.linalg.pinv(hidden.T @ hidden + self.gamma * np.identity(hidden.shape[1])) @ hidden.T @ ys

    def predict(self, xs: np.ndarray) -> np.ndarray:
        """Predict using the trained ELM

        Parameters
        ----------
        xs : np.ndarray
            Input values

        Returns
        -------
        np.ndarray
            Predicted output values
        """
        hidden = self.__forward(xs, self.w_in, self.bias)
        return np.dot(hidden, self.w_out)
