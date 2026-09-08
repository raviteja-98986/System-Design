from abc import ABC,abstractmethod


#observer
class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass

class User(Subscriber):
    def __init__(self,name):
        self.name=name

    def update(self, channel):
        print(f"{self.name} you received notification: New video '{channel.last_video}' from {channel.name}\n")

class YoutubeChannel:
    def __init__(self,name):
        self.name=name
        self.last_video=None
        self.subscribers=[]

    def subscribe(self,user):
        self.subscribers.append(user)

    def unsubscribe(self,user):
        self.subscribers.remove(user)

    def upload_video(self,video_title):
        self.last_video=video_title
        self.notify()

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self)

coder_Army=YoutubeChannel("Coder_Army")
apna_school=YoutubeChannel("Apna School")
teja=User("teja")
vishnu=User("Vishnu")
sai=User("sai")
pavan=User("pavan")

coder_Army.subscribe(teja)

coder_Army.subscribe(vishnu)

coder_Army.subscribe(sai)

coder_Army.subscribe(pavan)

apna_school.subscribe(vishnu)
apna_school.subscribe(sai)


coder_Army.upload_video("Observer Design Pattern")

apna_school.upload_video("Backtracking Playlist")