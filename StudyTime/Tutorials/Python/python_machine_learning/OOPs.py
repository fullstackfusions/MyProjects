# Class, Inheitance, Polymorphism, Encapsulation, Data Abstraction

from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Base Class for all ML models (Data Abstraction)
class MLModel(ABC):

    @abstractmethod
    def train(self, X, y=None):
        pass

    @abstractmethod
    def predict(self, X):
        pass

# Hierarchical Inheritance: Supervised and Unsupervised models
class SupervisedModel(MLModel):
    pass

class UnsupervisedModel(MLModel):
    pass

# Linear Regression - Supervised Learning
class LinearRegressionModel(SupervisedModel):

    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# KMeans Clustering - Unsupervised Learning
class KMeansModel(UnsupervisedModel):

    def __init__(self, n_clusters=2):
        self.model = KMeans(n_clusters=n_clusters)

    def train(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)

# Hybrid Inheritance: An advanced model that uses both supervised and unsupervised techniques
class AdvancedModel(LinearRegressionModel, KMeansModel):

    def __init__(self):
        LinearRegressionModel.__init__(self)
        KMeansModel.__init__(self, n_clusters=3)

    # Additional methods specific to AdvancedModel
