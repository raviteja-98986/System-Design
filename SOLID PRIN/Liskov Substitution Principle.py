from abc import ABC,abstractmethod

class NonWithdrawable(ABC):
    @abstractmethod
    def deposit():
        pass
class WithDrawable(NonWithdrawable):
    @abstractmethod
    def withdraw():
        pass
class SavingAccount(WithDrawable):
    def __init__(self,bal):
        self.__bal=bal
    @property
    def balance(self):
        return self.__bal
    def deposit(self,amt):
        if amt>0:
            self.__bal+=amt
        
    def withdraw(self,amt):
        if amt<self.balance:
            print(f"{amt} is debit in your Savings Account")
            self.__bal-=amt
        else:
            print("Insuffiecent amount")

class CurrentAccount(WithDrawable):
    def __init__(self,bal):
        self.__bal=bal
    @property
    def balance(self):
        return self.__bal
    def deposit(self,amt):
        if amt>0:
            self.__bal+=amt
        
    def withdraw(self,amt):
        if amt<self.balance:
            print(f"{amt} is debit in your Current Account")
            self.__bal-=amt
        else:
            print("Insuffiecent amount")
class FixedDepositAccount(NonWithdrawable):
    def __init__(self,bal):
        self.__bal=bal
    @property
    def balance(self):
        return self.__bal
    def deposit(self,amt):
        if amt>0:
            self.__bal+=amt
            print(f"{amt} is credit in your Fixed Deposit Account")
        
class BankClient():
    def __init__(self,depositonlyAccounts,withdrawableAccounts):
        self.DOA=list(depositonlyAccounts)
        self.WA=list(withdrawableAccounts)
    def process_transaction(self):
        for acc in self.DOA:
            acc.deposit(2000)
        for acc in self.WA:
            acc.deposit(1000)
 
            acc.withdraw(500)

fd=FixedDepositAccount(1000)
sa=SavingAccount(2000)
ca=CurrentAccount(3000)
b=BankClient([fd],[sa,ca])
b.process_transaction()