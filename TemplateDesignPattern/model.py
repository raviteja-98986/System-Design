#Template Method Pattern defines the fixed steps of an algorithm in a parent class, 
# while allowing child classes to provide their own implementation for some of those steps.

from abc import ABC, abstractmethod

# "Template Method Pattern fixes the algorithm's workflow in the parent class "
# "but lets subclasses customize individual steps."

class TrainModel(ABC):

    def load_dataset(self, data):
        print("Common: Loading the dataset")
        self.data = data

    def preprocess(self):
        print("Common: preprocessing the data")

    @abstractmethod
    def training(self):
        pass

    @abstractmethod
    def evaluating(self):
        pass

    @abstractmethod
    def save_Model(self):
        pass

    # Template Method
    def execute(self, data):
        self.load_dataset(data)
        self.preprocess()
        self.training()
        self.evaluating()
        self.save_Model()


class NeuralNetworkModel(TrainModel):

    def training(self):
        print("Training the Neural Network model")

    def evaluating(self):
        print("Evaluating Neural Network model")

    def save_Model(self):
        print("Saving Neural Network model")


class MLModel(TrainModel):

    def training(self):
        print("Training the ML model")

    def evaluating(self):
        print("Evaluating ML model")

    def save_Model(self):
        print("Saving ML model")


ml = MLModel()
ml.execute("dataset")

print("=" * 60)

nn = NeuralNetworkModel()
nn.execute("dataset")