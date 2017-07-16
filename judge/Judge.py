import subprocess
import time
from judge.Toolkit import *

class Judge:

    def __init__(self, src_script, src_txt):
        """Creates a new judge that is able to run"""
        self.raw_config = load_config('config.json')
        self.src_script = src_script
        self.src_txt = src_txt
        with open(src_script, 'r') as fp:
            self.script = fp.read()
        with open(src_txt, 'r') as fp:
            self.txt = fp.read()

    def run(self):
        output = None
        elapsed = -1
        lang = identify(self.src_script)
        command = (self.raw_config['about'][lang]['run'] % self.src_script).split(' ')

        with open(self.src_txt, 'r') as inlet:
            start = time.time()
            output = subprocess.check_output(command, stdin=inlet)
            elapsed = time.time() - start
        output = output.decode('utf-8').strip(' \r\n')
        return output, elapsed
