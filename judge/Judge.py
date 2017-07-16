import os
from judge.Toolkit import *

class Judge:
    raw_config = load_config('config.json')

    def __init__(self, src_script, src_txt):
        """Creates a new judge that is able to run"""
        self.src_script = src_script
        self.src_txt = src_txt
        with open(src_script, 'r') as fp:
            self.script = fp.read()
        with open(src_txt, 'r') as fp:
            self.txt = fp.read()

    def run(self):
        output = self.txt
        elapsed = 0.1
        return output, elapsed
