import unittest
import judge

class TestJudge(unittest.TestCase):
    def test_try_to_open_inexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge('randomscript', 'randominlet')

    def test_try_to_save_to_file_and_delete_afterwards(self):
        script = 'print(input())'
        txt = 'hello joe!'
        src_script = 'hello.py'
        src_txt = 'hello.txt'
        judge.Judge.save(src_script, script)
        judge.Judge.save(src_txt, txt)
        self.judge = judge.Judge(src_script, src_txt)
        self.assertIsNotNone(self.judge.script)
        self.assertIsNotNone(self.judge.txt)
        judge.Judge.delete(src_script)
        judge.Judge.delete(src_txt)
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge(src_script, src_txt)

if __name__ == '__main__':
    unittest.main()
