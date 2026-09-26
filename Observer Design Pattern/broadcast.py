from abc import ABC,abstractmethod



class Observer(ABC):
    @abstractmethod
    def broadcast(self):
        pass
class Observable(ABC):
    @abstractmethod
    def add_observer(self):
        pass
    @abstractmethod
    def remove_observer(self):
        pass
    @abstractmethod
    def notify(self):
        pass

class Notifier(Observable):
    def __init__(self):
        self.observers=[]
    def add_observer(self,obj):
       self.observers.append(obj)
    def remove_observer(self):
        self.oberservers.remove(obj)
    def notify(self,msg):
        for observer in self.observers:
            observer.broadcast(msg)
    def send_msg(self,msg):
        self.notify(msg)

class Whatsapp(Observer):
    def __init__(self,name,number):
        self.name=name
        self.number=number
        self.my_contancts=[]
    def broadcast(self,msg):
        for num in self.my_contancts:
            print(f"to:{num}  {msg} is broadcasting through whatsapp from {self.name} {self.number} ")
    def add_contact(self,num):
        self.my_contancts.append(num)
class Instagram(Observer):
    def __init__(self,id):
        self.id=id
        self.followers=[]
    def follow(self,id):
        self.followers.extend(id)
    def broadcast(self,msg):
        for id in self.followers:
            print(f"To:{id} {msg} is broadcasting through Instagram from {self.id}")

noti=Notifier()
wh=Whatsapp("teja","9493598986")
wh.add_contact("9676612433")
wh.add_contact("9493988766")
Ins=Instagram("t_e_j__a_a")
Ins.follow(["call_me_pandu","sai_teja","Mr_tej","rohith"])
noti.add_observer(wh)
noti.add_observer(Ins)
noti.notify("I am deactivating my instagram account")