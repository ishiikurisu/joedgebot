import unittest
import judge

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.script = '#! python\nprint(input())'
        self.txt = 'hello joe!'
        self.src_script = 'hello.py'
        self.src_txt = 'hello.txt'

    def test_try_to_open_inexistent_file(self):
        judge.Toolkit.delete('randomfile')
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge('randomscript', 'randominlet')

    def test_try_to_save_to_file_and_delete_afterwards(self):
        judge.Toolkit.save(self.src_script, self.script)
        judge.Toolkit.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        self.assertIsNotNone(self.judge.script)
        self.assertIsNotNone(self.judge.txt)
        judge.Toolkit.delete(self.src_script)
        judge.Toolkit.delete(self.src_txt)
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge(self.src_script, self.src_txt)

    def test_try_to_identify_languages(self):
        language = judge.Toolkit.identify(self.src_script)
        self.assertEqual('python', language)
        language = judge.Toolkit.identify('hello.rb')
        self.assertEqual('ruby', language)
        language = judge.Toolkit.identify('br.eng.crisjr.failproof.android.java')
        self.assertEqual('java', language)
        language = judge.Toolkit.identify('dog.c')
        self.assertEqual('c', language)
        with self.assertRaises(TypeError):
            language = judge.Toolkit.identify('func.fs')
        language = judge.Toolkit.get_bang(self.script)
        self.assertEqual('python', language)
        language = judge.Toolkit.get_bang('puts "hello joe"')
        self.assertIsNone(language)

    def test_runs_a_program(self):
        judge.Toolkit.save(self.src_script, self.script)
        judge.Toolkit.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        output, run_time = self.judge.run()
        self.assertEqual(output, self.txt)
        self.assertGreater(run_time, 0)
        judge.Toolkit.delete(self.src_script)
        judge.Toolkit.delete(self.src_txt)

    def test_fetches_a_program(self):
        txt = "2"
        src_txt = "double.txt"
        script = "puts(gets.chomp.to_i*2)"
        src_script = "double.rb"
        judge.Toolkit.save(src_script, script)
        judge.Toolkit.save(src_txt, txt)
        self.judge = judge.Judge(src_script, src_txt)
        output, run_time = self.judge.run()
        self.assertEqual(output, "4")
        self.assertGreater(run_time, 0)
        judge.Toolkit.delete(src_script)
        judge.Toolkit.delete(src_txt)


if __name__ == '__main__':
    unittest.main()
