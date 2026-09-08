class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        # Create object only if it doesn't exist
        if cls._instance is None:
            print("Creating Logger object")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        # Initialize only once
        if not self._initialized:
            print("Initializing Logger")

            self.log_file = "application.log"
            self.log_count = 0

            self._initialized = True

    def log(self, message):
        self.log_count += 1

        print(f"[LOG] {message}")


class LoginService:

    def login(self, username):
        logger = Logger()
        logger.log(f"{username} logged in")


class OrderService:

    def create_order(self, order_id):
        logger = Logger()
        logger.log(f"Order {order_id} created")


class PaymentService:

    def make_payment(self, amount):
        logger = Logger()
        logger.log(f"Payment of ₹{amount} completed")


# Application starts

login = LoginService()
order = OrderService()
payment = PaymentService()

login.login("Ravi")
order.create_order(101)
payment.make_payment(500)

# Check Singleton
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
print(logger1.log_count)
print(logger1.log_file)