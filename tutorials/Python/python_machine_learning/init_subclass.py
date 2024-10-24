## init_subclass method and subclass

class MLModel:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'MODEL_TYPE'):
            raise AttributeError(f"{cls.__name__} must define 'MODEL_TYPE' attribute")
        if not callable(getattr(cls, "train", None)):
            raise AttributeError(f"{cls.__name__} must implement a 'train' method")

    def train(self):
        raise NotImplementedError("Subclasses must implement the train method")

class RandomForest(MLModel):
    MODEL_TYPE = "Random Forest"

    def train(self, data):
        print(f"Training {self.MODEL_TYPE} model with data")

class NeuralNetwork(MLModel):
    MODEL_TYPE = "Neural Network"

    def train(self, data):
        print(f"Training {self.MODEL_TYPE} model with data")

class SVM(MLModel):  # Missing MODEL_TYPE and train method
    pass

# Usage
random_forest = RandomForest()
random_forest.train(data="Sample Data")

neural_network = NeuralNetwork()
neural_network.train(data="Sample Data")

try:
    svm = SVM()  # This will raise an AttributeError
except AttributeError as e:
    print(e)
