from abc import ABC, abstractmethod


# Receiver
class Database:

    def insert(self, data):
        print(f"Inserted: {data}")

    def update(self, data):
        print(f"Updated: {data}")

    def delete(self, data):
        print(f"Deleted: {data}")


# Command
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class InsertCommand(Command):

    def __init__(self, database, data):
        self.database = database
        self.data = data

    def execute(self):
        self.database.insert(self.data)


class UpdateCommand(Command):

    def __init__(self, database, data):
        self.database = database
        self.data = data

    def execute(self):
        self.database.update(self.data)


class DeleteCommand(Command):

    def __init__(self, database, data):
        self.database = database
        self.data = data

    def execute(self):
        self.database.delete(self.data)


# Invoker
class CommandExecutor:

    def set_command(self, command):
        self.command = command

    def execute(self):
        self.command.execute()


# Client
database = Database()

executor = CommandExecutor()

executor.set_command(
    InsertCommand(database, "Ravi")
)

executor.execute()

executor.set_command(
    UpdateCommand(database, "Ravi Kumar")
)

executor.execute()

executor.set_command(
    DeleteCommand(database, "Ravi Kumar")
)

executor.execute()