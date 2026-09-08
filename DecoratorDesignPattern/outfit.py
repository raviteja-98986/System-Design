from abc import ABC, abstractmethod


# Component
class Person(ABC):

    @abstractmethod
    def dress(self):
        pass


# Concrete Component
class BasicPerson(Person):

    def dress(self):
        print("T-Shirt is wearing")


# Base Decorator
class PersonDecorator(Person):

    def __init__(self, person):
        self.person = person

    def dress(self):
        self.person.dress()


# Concrete Decorator
class LayeringDecorator(PersonDecorator):

    def dress(self):
        self.person.dress()
        print("Layering with shirt")


# Concrete Decorator
class ChainDecorator(PersonDecorator):

    def dress(self):
        self.person.dress()
        print("Wearing chain")


# Concrete Decorator
class RingDecorator(PersonDecorator):

    def dress(self):
        self.person.dress()
        print("Wearing Ring")


# Concrete Decorator
class GlassesDecorator(PersonDecorator):

    def dress(self):
        self.person.dress()
        print("Styling with cooling glasses")

person = BasicPerson()

person = GlassesDecorator(person)

person = LayeringDecorator(person)

person = ChainDecorator(person)

person = RingDecorator(person)

person.dress()

RingDecorator(
    ChainDecorator(
        GlassesDecorator(
            BasicPerson()
        )
    )
)