class Insta:
    ids=[]
    def __init__(self,id):
        if id not in Insta.ids:
            Insta.ids.append(id)
            self.id=id
            self.followers=[]
            self.following=[]
        else:
            raise ValueError("Id already exists")

    def follow(self,acc):
        self.following.append(acc)
        acc.followers.append(self)

    def unfollow(self,acc):
        self.followers.remove(acc)
        acc.following.remove(acc)

    def details(self):
        print(f"{self.id} follower:{len(self.followers)} following:{len(self.following)}")
        print(f"followers:{self.followers}")
        print(f"following:{self.following}")

    def __repr__(self):
        return self.id
    

teja=Insta("teja")
gopi=Insta("md_gopal")
siva=Insta("call_me_pandu")
rohith=Insta("RohithKumar")
satish=Insta("Satish__")
teja.follow(gopi)
teja.follow(rohith)
teja.follow(satish)
satish.follow(teja)
siva.follow(teja)
teja.details()
arjun=Insta("arjun_tej")

print(Insta.ids)    
