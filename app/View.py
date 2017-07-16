class View:
    def __init__(self, controller):
        self.step = -1
        self.finished = False
        self.controller = controller

    def ask(self, question):
        if self.step == 0:
            if question == '/cancel':
                self.finished = True
                return 'ok'
            else:
                self.step = 1
                # TODO Process sent script
                return 'text:'
        elif self.step == 1:
            if question == '/cancel':
                self.finished = True
                return 'ok'
            else:
                self.step = -1
                self.finished = True
                # TODO Run the script!
                return '4'
        else:
            if question == '/start':
                self.step = 0
                return 'script:'
            else:
                return 'what?'
