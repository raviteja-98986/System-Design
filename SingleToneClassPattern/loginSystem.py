class Logger:
    _instance=None
    _initialized=False
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not self._initialized:
            print("Logger is Initializing")
            self._initialized=True
            self.log_count=0
            self.log_file="Application_Logger"
    def log(self,msg):
        with open(self.log_file,"a+") as f:
            msg=f"{msg}\n"
            f.write(msg)

    def print_log(self):
        with open(self.log_file,"r") as f:
            print(f.read())

class LoginPage:
    def login(self,name,pwd):
        msg=f"user:{name} is loggedIn"
        logger=Logger()
        logger.log(msg)

class Order:
    def order(self,id,prod):
        msg=f"{prod} is ordered with order id {id}"
        logger=Logger()
        logger.log(msg)

class Delivered:
    def deliver(self,id,prod):
        msg=f"{prod} is delivered with order id {id}"
        logger=Logger()
        logger.log(msg)

login=LoginPage()
login.login('teja',123)
order=Order()
order.order(9887,'T-shirt')
d=Delivered()
d.deliver(2354,'Shoes')
l1=Logger()
l2=Logger()
print(l1 is l2)
l1.print_log()