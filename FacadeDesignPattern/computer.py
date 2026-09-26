class CPU:
    def freeze(self):
        print("CPU freezing")

    def jump(self, position):
        print(f"CPU jumping to {position}")

    def execute(self):
        print("CPU executing")


class Memory:
    def load(self, position, data):
        print(f"Loading {data} into {position}")


class HardDrive:
    def read(self, sector, size):
        print(f"Reading {size} bytes from sector {sector}")
#Without Facade, the client has to know everything:
# cpu = CPU()
# memory = Memory()
# hard_drive = HardDrive()

# boot_address = 100

# hard_drive.read(0, 1024)
# memory.load(boot_address, "BOOT_DATA")
# cpu.freeze()
# cpu.jump(boot_address)
# cpu.execute()

# using Facade Design pattern

class ComputerFacade:

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.hard_drive.read(0, 1024)
        self.memory.load(100, "BOOT_DATA")
        self.cpu.freeze()
        self.cpu.jump(100)
        self.cpu.execute()

computer = ComputerFacade()

computer.start_computer()