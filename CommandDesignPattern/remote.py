from abc import ABC,abstractmethod
class Icommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is on")
    def off(self):
        print("Light is off")

class Fan:
    def on(self):
        print("Fan is on")
    def off(self):
        print("Fan is off")

class LightCmd(Icommand):
    def __init__(self,light):
        self.light=light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class FanCmd(Icommand):
    def __init__(self,fan):
        self.fan=fan
    def execute(self):
        self.fan.on()
    def undo(self):
        self.fan.off()

class Remote:
    def __init__(self,cmds,no_btns):
        self.btns=cmds
        self.btns_status=[False]*no_btns
    def press_btn(self,btn_no):

        if btn_no>=0 and btn_no<len(self.btns_status):
            if not self.btns_status[btn_no]:
                self.btns_status[btn_no]=True
                self.btns[btn_no].execute() 
            else:
                self.btns_status[btn_no]=False
                self.btns[btn_no].undo()
fan=Fan()
fan_cmd=FanCmd(fan)
light=Light()
light_cmd=LightCmd(light)
re=Remote([fan_cmd,light_cmd],2)
re.press_btn(0)
re.press_btn(1)
re.press_btn(0)
re.press_btn(1)
re.press_btn(1)