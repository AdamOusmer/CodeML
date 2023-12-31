import numpy as np
from src.neural_network.model import Model
from sklearn.model_selection import train_test_split as sk_split


class NeuralNetwork:

    def __init__(self, dataset: np.ndarray = None, model: Model = None, test_size: float = 0.2, size: int = 10):

        self.test_size = test_size
        self.size = size

        if dataset is not None:
            self.dataset = dataset
            self.train, self.test = sk_split(dataset, test_size=self.test_size, shuffle=True)
        else:
            raise ValueError("Dataset is None")

        self.model: Model = model if model is not None else Model(self.train, self.test)

    def train_nn(self):
        self.model.train_model()

    def test_nn(self):
        self.model.test_model()

    def predict_nn(self, data: np.ndarray):
        return self.model.predict_model(data)
