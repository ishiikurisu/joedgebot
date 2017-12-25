import unittest
import subprocess
import judge

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.script = '#! python\nprint(input())'
        self.txt = 'hello joe!'
        self.src_script = 'hello.py'
        self.src_txt = 'hello.txt'

    def tearDown(self):
        pass

    def test_cli_can_give_you_help(self):
        output = subprocess.check_output(['./cli.exe'], stderr=subprocess.STDOUT).decode('utf-8').strip()
        self.assertEqual(output, 'Arguments missing!')

    def test_cli_can_run_a_python_program(self):
        judge.Toolkit.save(self.src_script, self.script)
        judge.Toolkit.save(self.src_txt, self.txt)
        output = subprocess.check_output(['./cli.exe', self.src_script, self.src_txt],
                                         stderr=subprocess.STDOUT).decode('utf-8').strip()
        self.assertEqual(output, self.txt)
        judge.Toolkit.delete(self.src_script)
        judge.Toolkit.delete(self.src_txt)

    def test_cli_can_run_a_ruby_program(self):
        src_script = "hello.rb"
        script = "puts gets.chomp"
        judge.Toolkit.save(src_script, script)
        judge.Toolkit.save(self.src_txt, self.txt)
        output = subprocess.check_output(['./cli.exe', src_script, self.src_txt],
                                         stderr=subprocess.STDOUT).decode('utf-8').strip()
        self.assertEqual(output, self.txt)
        judge.Toolkit.delete(src_script)
        judge.Toolkit.delete(self.src_txt)

if __name__ == '__main__':
    unittest.main()
