from abc import ABC, abstractmethod


class FileSystem(ABC):

    @abstractmethod
    def show(self, space=0):
        pass


class File(FileSystem):

    def __init__(self, name):
        self.name = name

    def show(self, space=0):
        print("   " * space + self.name)


class Folder(FileSystem):

    def __init__(self, name):
        self.name = name
        self.files = []

    def show(self, space=0):
        print("   " * space + "+ " + self.name)

        for item in self.files:
            item.show(space + 1)

    def add_files(self, files):
        self.files.extend(files)


project = Folder("Project")

model = File("models.py")
url = File("urls.py")

templates = Folder("Templates")

home = File("home.html")
db = File("Dashboard.html")

templates.add_files([home, db])
project.add_files([model, url, templates])

project.show()