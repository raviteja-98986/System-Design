from abc import ABC, abstractmethod


# --------------------------------
# 1. Product
# --------------------------------

class Shirt(ABC):

    @abstractmethod
    def wear(self):
        pass


# --------------------------------
# 2. Concrete Products
# --------------------------------

class Tshirt(Shirt):

    def wear(self):
        print("Wearing T-shirt")


class FormalShirt(Shirt):

    def wear(self):
        print("Wearing Formal Shirt")


class ChecksShirt(Shirt):

    def wear(self):
        print("Wearing Checks Shirt")


# --------------------------------
# 3. Creator
# --------------------------------
class ShirtCreators(ABC):
    @abstractmethod
    def get_obj(self):
        pass
    def create(self):
        return self.get_obj()

class TshirtCreator(ShirtCreators):
    def get_obj(self):
        return Tshirt()


class FormalShirtCreator(ShirtCreators):
    def get_obj(self):
        return FormalShirt()

class ChecksShirtCreator(ShirtCreators):
    def get_obj(self):
        return ChecksShirt()

shirt=TshirtCreator()
tshirt=shirt.create()
tshirt.wear()
