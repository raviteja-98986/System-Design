class PaymentProcessor(ABC):

    def process_payment(self):
        self.validate()
        self.authenticate()
        self.make_payment()
        self.save_transaction()

    def validate(self):
        print("Validating payment")

    def authenticate(self):
        print("Authenticating user")

    @abstractmethod
    def make_payment(self):
        pass

    def save_transaction(self):
        print("Saving transaction")


class UPI(PaymentProcessor):

    def make_payment(self):
        print("Making UPI payment")


class CreditCard(PaymentProcessor):

    def make_payment(self):
        print("Making Credit Card payment")