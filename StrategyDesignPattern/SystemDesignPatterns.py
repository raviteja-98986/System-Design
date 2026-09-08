#when there are multiple ways of doing something, put each way into a separate class and 
# allow us to choose which one to use
from abc import ABC,abstractmethod
class MovementStrategy(ABC):
    @abstractmethod
    def move(self):
        pass

class WalkStrategy(MovementStrategy):
    def move(self):
        print("Robot is Walking ")

class JumpingStrategy(MovementStrategy):
    def move(self):
        print("Robot is jumping")

class RunningStrategy(MovementStrategy):
    def move(self):
        print("Robot is Running ")

class Robot:

    def __init__(self,name,strategy):
        self.name=name
        self.strategy=strategy

    def strategy(self,strategy):
        self.strategy=strategy

    def move(self):
        self.strategy.move()

chitti=Robot("chitti",WalkStrategy())
chitti.move()
chitti=Robot("chitti",RunningStrategy())
chitti.move()