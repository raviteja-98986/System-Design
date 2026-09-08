from abc import ABC,abstractmethod
class Shirt(ABC):
    @abstractmethod
    def shirt(self):
        pass
class Pant(ABC):
    @abstractmethod
    def pant(self):
        pass

class FormalShirt(Shirt):
    def shirt(self):
        print("Formal shirt")

class Tshirt(Shirt):
    def shirt(self):
        print("Tshirt ")

class Checks(Shirt):
    def shirt(self):
        print("Checks shirt")

class Baggy(Pant):
    def pant(self):
        print("Baggy pant")

class FormalPant(Pant):
    def pant(self):
        print("FormalPant")

class Cargo(Pant):
    def pant(self):
        print("Cargo Pant")


class Men:
    def __init__(self,shirt,pant):
        self.shirt=shirt
        self.pant=pant
    def  change_shirt(self,shirt):
        self.shirt=shirt
    def change_pant(self,pant):
        self.pant=pant

class Student(Men):
    def outfit(self):
        self.shirt.shirt()
        self.pant.pant()

obj=Student(Tshirt(),Cargo())
obj.outfit()
obj.change_shirt(Checks())
obj.outfit()