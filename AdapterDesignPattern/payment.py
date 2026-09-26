from abc import ABC, abstractmethod


class PaymentAdapter(ABC):

    @abstractmethod
    def pay(self, amt):
        pass


class Razorpay:
    def make_payment(self,amt):
        print(f"{amt} Razorpay payment")

class Stripe:
    def execute_payment(self,amt):
        print(f"{amt} Stripe payment")

class RazorpayAdapter(PaymentAdapter):
    def __init__(self):
        self.razo=Razorpay()
    def pay(self,amt):
        self.razo.make_payment(amt)

class StripeAdapter(PaymentAdapter):
    def __init__(self):
        self.stripe=Stripe()
    def pay(self,amt):
        self.stripe.execute_payment(amt)

class Payment:
    def __init__(self,adapter):
        self.adapter=adapter
    def pay(self,amt):
        self.adapter.pay(amt)

adapter=StripeAdapter()
payment=Payment(adapter)
payment.pay(500)