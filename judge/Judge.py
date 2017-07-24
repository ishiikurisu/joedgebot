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
        """Builds and runs the provided scripts"""
        output = None
        elapsed = -1

        # Building
        lang = identify(self.src_script)
        kind = self.raw_config['about'][lang]['kind']
        if kind == 'interpreted':
            raw_command = self.raw_config['about'][lang]['run']
            command = (raw_command % self.src_script).split(' ')
        elif kind == 'compiled':
            raw_build = self.raw_config['about'][lang]['build']
            build = (raw_build % self.src_script).split(' ')
            subprocess.check_output(build)
            raw_command = self.raw_config['about'][lang]['run']
            command = (raw_command % self.src_script).split(' ')


        # Executing
        with open(self.src_txt, 'r') as inlet:
            start = time.time()
            # TODO Collect stderr for displaying it whenever necessary
            output = subprocess.check_output(command, stdin=inlet)
            elapsed = time.time() - start
        output = output.decode('utf-8').strip(' \r\n')
        return output, elapsed
