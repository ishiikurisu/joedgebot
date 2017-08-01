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

    def run(self):
        """Builds and runs the provided scripts"""
        output = None
        elapsed = -1

        # Cleaning source code
        if self.script.split('\n')[0][0:2] == '#!':
            with open(self.src_script, 'w') as fp:
                fp.write('\n'.join(self.script.split('\n')[1:]))

        # Building
        lang = identify(self.src_script)
        kind = self.raw_config['about'][lang]['kind']
        if kind == 'interpreted':
            raw_command = self.raw_config['about'][lang]['run']
            command = (raw_command.format(self.src_script)).split(' ')
        elif kind == 'compiled':
            raw_build = self.raw_config['about'][lang]['build']
            build = (raw_build.format(self.src_script)).split(' ')
            try:
                subprocess.check_output(build, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                return e.output, elapsed
            raw_command = self.raw_config['about'][lang]['run']
            command = (raw_command.format(self.src_script)).split(' ')
        else:
            raise AttributeError()

        # Executing
        with open(self.src_txt, 'r') as inlet:
            try:
                start = time.time()
                output = subprocess.check_output(command, stdin=inlet, stderr=subprocess.STDOUT)
                elapsed = time.time() - start
                output = output.decode('utf-8').strip(' \r\n')
            except subprocess.CalledProcessError as e:
                output = e.output
                elapsed = -1

        return output, elapsed
