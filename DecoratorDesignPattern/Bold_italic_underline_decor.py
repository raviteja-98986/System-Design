from abc import ABC,abstractmethod

class Text(ABC):
    @abstractmethod
    def render(self):
        pass

class PlainText(ABC):
    def __init__(self,text):
        self.text=text
    def render(self):
        return self.text

class TextDecor(PlainText):
    def __init__(self,text):
        self.text=text

    def render(self):
        return self.text.render()
    
class BoldDecor(TextDecor):
    def render(self):
        return "<b>" + self.text.render() + "</b>"

class ItalicDecor(TextDecor):
    def render(self):
        return "<i>" + self.text.render() + "</i>"

class UnderlineDecor(TextDecor):
    def render(self):
        return "<u>" + self.text.render() + "</u>"

# text=PlainText('Hello world')
# italic=ItalicDecor(text)
# bold=BoldDecor(italic)
# print(bold.render())
text=UnderlineDecor(BoldDecor(ItalicDecor(PlainText("hello"))))
print(text.render())