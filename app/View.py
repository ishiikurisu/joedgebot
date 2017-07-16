class View:
    def __init__(self, controller):
        self.step = -1
        self.finished = False
        self.controller = controller
        self.language = None

    def ask(self, question):
        if self.step == 0:
            if question == '/cancel':
                self.finished = True
                return 'ok'
            else:
                self.step = 1
                self.language = self.controller.understand(question)
                self.controller.save_script(question, language)
                return 'text:'
        elif self.step == 1:
            if question == '/cancel':
                self.finished = True
                return 'ok'
            else:
                self.step = -1
                self.finished = True
                self.controller.save_text(question)
                return self.controller.run()
        else:
            if question == '/start':
                self.step = 0
                return 'script:'
            else:
                return 'what?'
