import os

class Judge:
    def __init__(self, src_script, src_txt):
        self.src_script = src_script
        self.src_txt = src_txt
        with open(src_script, 'r') as fp:
            self.script = fp.read()
        with open(src_txt, 'r') as fp:
            self.txt = fp.read()

    def save(where, what):
        with open(where, 'w') as fp:
            fp.write(what)

    def delete(what):
        os.remove(what)
