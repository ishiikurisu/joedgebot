from app.Model import *
from app.View import *

class Controller:
    def __init__(self):
        self.ids = { }

    def listen(self, id, question):
        if id not in self.ids:
            self.ids[id] = self.new_mv()
        view = self.ids[id]['view']
        output = view.ask(question)
        if view.finished:
            del self.ids[id]
        return output

    def new_mv(self):
        return {
            'view': View(self)
        }
