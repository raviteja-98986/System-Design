from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass

class Notifier(Notification):
    def __init__(self,msg):
        self.msg=msg
    def notify(self):
         return f"{self.msg} "

class NotificationDecor(Notification):
    def __init__(self,app):
        self.app=app

    def notify(self):
        self.app.notify()

class WhatsappDecor(NotificationDecor):
    def notify(self):
        
        return self.app.notify() + f"send through whatsapp "

class FacebookDecor(NotificationDecor):
    def notify(self):
        return self.app.notify()+f"send through facebook"
        

msgr=FacebookDecor(WhatsappDecor(Notifier("hello")))
    
print(msgr.notify())