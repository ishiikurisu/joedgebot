from app.Model import *
from app.View import *

class Controller:
    def __init__(self):
        self.ids = { }

    def listen(self, name, question):
        if name not in self.ids:
            self.ids[name] = self.new_mv(name)
        view = self.ids[name]['view']
        output = view.ask(question)
        if view.finished:
            del self.ids[name]
        return output

    def new_mv(self, name):
        return {
            'view': View(self, name)
        }

    def understand(self, script):
        return Model.understand(script)

    def save_script(self, name, script, language):
        extension = Model.extend(language)
        filename = '%d.%s' % (name, extension)
        Model.save_script(filename, script)
        return filename

    def save_text(self, name, text):
        self.save_script(name, text, 'text')

    def clean(self, name):
        Model.clean(str(name) + '.txt')
        Model.clean(str(name) + '.' + Model.extend(self.ids[name]['view'].language))

    def run(self, name):
        script = '%d.%s' % (name, Model.extend(self.ids[name]['view'].language))
        text = str(name) + '.txt'
        Model.check_existence(script)
        Model.check_existence(text)
        output, run_time = Model.run(script, text)
        return output
