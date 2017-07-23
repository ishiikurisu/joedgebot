class View:
    def __init__(self, controller, name):
        self.step = -1
        self.finished = False
        self.controller = controller
        self.language = None
        self.name = name

    def ask(self, question):
        if self.step == 0:
            if question == '/cancel':
                self.clean(self.name)
                self.finished = True
                return 'ok'
            else:
                self.step = 1
                self.language = self.controller.understand(question)
                self.controller.save_script(self.name, question, self.language)
                return 'text:'
        elif self.step == 1:
            self.finished = True
            if question == '/cancel':
                self.clean()
                return 'ok'
            else:
                self.step = -1
                self.controller.save_text(self.name, question)
                output = self.controller.run(self.name)
                self.clean()
                return output
        else:
            if question == '/start':
                self.step = 0
                return 'script:'
            else:
                return 'what?'

    def clean(self):
        self.controller.clean(self.name)
