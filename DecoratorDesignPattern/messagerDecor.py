from abc import ABC,abstractmethod
from datetime import datetime
class IMessager(ABC):
    @abstractmethod
    def send(self):
        pass

class Messanger(IMessager):
    def __init__(self,msg):
        self.msg=msg
    def send(self):
        return f"{self.msg} "
class MessagerDecor:
    def __init__(self,feature):
        self.feature=feature
    def send(self):
        return self.feature.send()
class TimeStamp(MessagerDecor):
    def send(self):
        date=datetime.now()
        return f"{date} "+self.feature.send()
class Signature(MessagerDecor):
    def send(self):
        return f"signature is added "+self.feature.send()

msg = Signature(
          TimeStamp(
              Messanger("Hi hello")
          )
      )

print(msg.send())
