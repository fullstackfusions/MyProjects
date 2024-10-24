## ABC class and Abstract method with Production level practice

from abc import ABC, abstractmethod
from typing import Any, Dict

class MLModel(ABC):
    """
    Abstract base class for a machine learning model.
    """

    @abstractmethod
    def train(self, X, y) -> None:
        """
        Train the model on the given data.

        Parameters:
        X: Training data features
        y: Training data labels/target values
        """
        pass

    @abstractmethod
    def predict(self, X) -> Any:
        """
        Predict the target values for the given test data.

        Parameters:
        X: Test data features

        Returns:
        Predictions for the test data.
        """
        pass

    @abstractmethod
    def save_model(self, path: str) -> None:
        """
        Save the trained model to a file.

        Parameters:
        path: Path to save the model.
        """
        pass

    @abstractmethod
    def load_model(self, path: str) -> None:
        """
        Load a model from a file.

        Parameters:
        path: Path to load the model from.
        """
        pass

from sklearn.linear_model import LinearRegression
import joblib

class SimpleLinearRegression(MLModel):
    """
    Simple linear regression model.
    """

    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y) -> None:
        if X is None or y is None:
            raise ValueError("Training data cannot be None")
        self.model.fit(X, y)

    def predict(self, X) -> Any:
        if X is None:
            raise ValueError("Test data cannot be None")
        return self.model.predict(X)

    def save_model(self, path: str) -> None:
        joblib.dump(self.model, path)

    def load_model(self, path: str) -> None:
        self.model = joblib.load(path)
