## @property @abstractmethod

"""
The @property decorator in Python is a built-in decorator used for defining property attributes. It turns a method into a "getter" for a read-only attribute with the same name. This can be particularly useful in machine learning for encapsulating model attributes, ensuring that they are read-only, or providing a calculated property based on other attributes.
"""

# @property
class LinearRegressionModel:
    def __init__(self, weights, bias):
        self._weights = weights
        self._bias = bias

    @property
    def weights(self):
        """Returns the weights of the model. Read-only."""
        return self._weights

    @property
    def bias(self):
        """Returns the bias of the model. Read-only."""
        return self._bias

    @property
    def parameters(self):
        """Calculates and returns the number of parameters in the model."""
        return len(self._weights) + 1

    # Additional methods for the model, like fit, predict, etc.


# @abstract_method

from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def parameters(self):
        """Returns the number of parameters in the model. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def fit(self, X, y):
        """Fit the model to the data. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def predict(self, X):
        """Predict using the model. Must be implemented by subclasses."""
        pass

# In subclass
class LinearRegressionModel(BaseModel):
    def __init__(self, weights, bias):
        super().__init__()
        self._weights = weights
        self._bias = bias

    @property
    def weights(self):
        return self._weights

    @property
    def bias(self):
        return self._bias

    @property
    def parameters(self):
        return len(self._weights) + 1

    def fit(self, X, y):
        # Implementation of fitting logic
        pass

    def predict(self, X):
        # Implementation of prediction logic
        pass
