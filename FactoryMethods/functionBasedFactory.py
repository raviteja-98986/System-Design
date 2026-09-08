from abc import ABC,abstractmethod
from FactoryMethods.functionBasedFactory import Burger

class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class VegBurger(Burger):
    pass

class NonVegBurger(Burger):
    pass

class BasicVegBurger(VegBurger):
    def prepare(self):
        print("Basic Veg Burger")

class StandardVegBurger(VegBurger):
    def prepare(self):
        print("StandardBurger Veg Burger")

class PremiumVegBurger(VegBurger):
    def prepare(self):
        print("StandardBurger Veg Burger")
#Non-veg burgers
class BasicNonVegBurger(NonVegBurger):
    def prepare(self):
        print("Basic NonVegBurgerr")

class StandardNonVegBurger(NonVegBurger):
    def prepare(self):
        print("StandardBurger NonVegBurger")

class PremiumNonVegBurger(NonVegBurger):
    def prepare(self):
        print("StandardBurger NonVegBurger")

#Burger Factory

class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self):
        pass

class VegBurgerFactory(BurgerFactory):

    def create_burger(self, burger_type):

        if burger_type == "basic":
            return BasicVegBurger()

        elif burger_type == "standard":
            return StandardVegBurger()

        elif burger_type == "premium":
            return PremiumVegBurger()

        else:
            raise ValueError("Invalid Veg Burger type")

class NonVegBurgerFactory(BurgerFactory):

    def create_burger(self, burger_type):

        if burger_type == "basic":
            return BasicNonVegBurger()

        elif burger_type == "standard":
            return StandardNonVegBurger()

        elif burger_type == "premium":
            return PremiumNonVegBurger()

        else:
            raise ValueError("Invalid Non-Veg Burger type")

veg_factory=VegBurgerFactory()
burger=veg_factory.create_burger('basic')
burger.prepare()
