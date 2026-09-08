from abc import ABC,abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class Observable(ABC):

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Investor(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, stock):
        print(
            f"{self.name}: {stock.name} price changed to {stock.price}"
        )

class TradingApp(Observer):

    def update(self, stock):
        print(
            f"Trading App: {stock.name} is now {stock.price}"
        )

class PriceAlert(Observer):

    def __init__(self, target_price):
        self.target_price = target_price

    def update(self, stock):

        if stock.price >= self.target_price:
            print(
                f"ALERT: {stock.name} reached {stock.price}"
            )
    def set_target(self,price):
        self.target_price=price

class Stock(Observable):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_price(self, price):
        self.price = price

        # Price changed
        self.notify()

tcs = Stock("TCS", 3500)

ravi = Investor("Ravi")
trading_app = TradingApp()
alert = PriceAlert(3600)

tcs.add_observer(ravi)
tcs.add_observer(trading_app)
tcs.add_observer(alert)

tcs.set_price(3700)