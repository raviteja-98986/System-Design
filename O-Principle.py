from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class Gpay(Payment):
    def pay(self,amt):
        print(f"{amt} is paying through Gpay")

class PhonePay(Payment):
    def pay(self,amt):
        print(f"{amt} is paying through PhonePay")

class Paytm(Payment):
    def pay(self,amt):
        print(f"{amt} is paying through paytm")

class NaviPay(Payment):
    def pay(self,amt):
        print(f"{amt} is paying from NaviPay")

class ElectricBill(Payment):
    def __init__(self,bill_no,amt):
        self.bill_no=bill_no
        self.amt=amt
    def pay(self,obj,amt):
        obj.pay(amt)

bill=ElectricBill(1234,549)
pay=Paytm()
navi=NaviPay()
amt=549
bill.pay(navi,amt)