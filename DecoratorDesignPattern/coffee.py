class SimpleCoffee:
    
    def cost(self):
        return 50


class MilkDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


class SugarDecorator:

    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 5

price=SugarDecorator(SimpleCoffee()).cost()

print(price)