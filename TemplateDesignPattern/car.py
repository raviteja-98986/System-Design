class CarManufacturer(ABC):

    def manufacture(self):
        self.design()
        self.build_body()
        self.install_engine()
        self.install_interior()
        self.test()

    def design(self):
        print("Designing car")

    def build_body(self):
        print("Building car body")

    @abstractmethod
    def install_engine(self):
        pass

    @abstractmethod
    def install_interior(self):
        pass

    def test(self):
        print("Testing car")

class ElectricCar(CarManufacturer):

    def install_engine(self):
        print("Installing electric motor")

    def install_interior(self):
        print("Installing EV interior")


class PetrolCar(CarManufacturer):

    def install_engine(self):
        print("Installing petrol engine")

    def install_interior(self):
        print("Installing petrol car interior")