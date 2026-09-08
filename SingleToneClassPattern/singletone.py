class PrimeMinister:
    instance=None

    def __new__(cls):
        if PrimeMinister.instance is None:
            PrimeMinister.instance=super().__new__(cls)

        return PrimeMinister.instance
    def __init__(self):
        print("Initialized")

obj1=PrimeMinister()
obj2=PrimeMinister()
print(obj1 is obj2)
    