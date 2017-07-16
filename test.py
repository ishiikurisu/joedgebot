import unittest
import judge

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.script = 'print(input())'
        self.txt = 'hello joe!'
        self.src_script = 'hello.py'
        self.src_txt = 'hello.txt'

    def test_try_to_open_inexistent_file(self):
        judge.Judge.delete('randomfile')
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge('randomscript', 'randominlet')

    def test_try_to_save_to_file_and_delete_afterwards(self):
        judge.Judge.save(self.src_script, self.script)
        judge.Judge.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        self.assertIsNotNone(self.judge.script)
        self.assertIsNotNone(self.judge.txt)
        judge.Judge.delete(self.src_script)
        judge.Judge.delete(self.src_txt)
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge(self.src_script, self.src_txt)

    def test_try_to_identify_languages(self):
        language = judge.Judge.identify(self.src_script)
        self.assertEqual('python', language)
        language = judge.Judge.identify('hello.rb')
        self.assertEqual('ruby', language)
        language = judge.Judge.identify('br.eng.crisjr.failproof.android.java')
        self.assertEqual('java', language)
        language = judge.Judge.identify('dog.c')
        self.assertEqual('c', language)
        with self.assertRaises(TypeError):
            language = judge.Judge.identify('func.fs')

    def test_runs_a_program(self):
        judge.Judge.save(self.src_script, self.script)
        judge.Judge.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        output, run_time = self.judge.run()
        self.assertEqual(output, self.txt)
        self.assertGreater(run_time, 0)
        judge.Judge.delete(self.src_script)
        judge.Judge.delete(self.src_txt)


if __name__ == '__main__':
    unittest.main()
