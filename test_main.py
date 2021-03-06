import unittest
import judge
import app

class TestJudge(unittest.TestCase):
    def setUp(self):
        self.script = '#! python\nprint(input())'
        self.txt = 'hello joe!'
        self.src_script = 'hello.py'
        self.src_txt = 'hello.txt'

    def test_try_to_use_an_inexistent_config_file(self):
        self.assertIsNone(judge.Toolkit.load_config('randomconfig'))
        judge.Toolkit.save(self.src_script, self.script)
        judge.Toolkit.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        self.judge.set_config('randomconfig')
        with self.assertRaises(RuntimeError):
            self.judge.run()
        judge.Toolkit.delete(self.src_script)
        judge.Toolkit.delete(self.src_txt)

    def test_try_to_open_inexistent_file(self):
        judge.Toolkit.delete('randomfile')
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge('randomscript', 'randominlet')

    def test_try_to_save_to_file_and_delete_afterwards(self):
        judge.Toolkit.save(self.src_script, self.script)
        judge.Toolkit.save(self.src_txt, self.txt)
        self.judge = judge.Judge(self.src_script, self.src_txt)
        self.assertIsNotNone(self.judge.script)
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

    def test_generate_correct_extension(self):
        self.assertEqual('py', judge.Toolkit.extend('python'))
        self.assertEqual('rb', judge.Toolkit.extend('ruby'))

    def test_raises_error_when_running_an_invalid_script(self):
        txt = "hi"
        src_txt = "error.txt"
        script = "#! ruby\ntext = gets.chomp\nputs text.upcas\n"
        src_script = "error.rb"
        judge.Toolkit.save(src_script, script)
        judge.Toolkit.save(src_txt, txt)
        self.judge = judge.Judge(src_script, src_txt)
        output, how_long = self.judge.run()
        self.assertEqual(-1, how_long)
        judge.Toolkit.delete(src_script)
        judge.Toolkit.delete(src_txt)

    def test_run_a_golang_program(self):
        script = """
package main
import "fmt"
func main() {
    fmt.Println("hello joe!")
}
        """
        txt = "asdf"
        script_file = "test.go"
        txt_file = "test.txt"
        judge.Toolkit.save(script_file, script)
        judge.Toolkit.save(txt_file, txt)
        self.judge = judge.Judge(script_file, txt_file)
        output, how_long = self.judge.run()
        self.assertEqual(output, "hello joe!")
        judge.Toolkit.delete(script_file)
        judge.Toolkit.delete(txt_file)

    def test_run_a_lua_script(self):
        script = """
line = io.read("*line")
io.write(line, "\\n")
"""
        txt = "hello joe\n"
        script_file = "test.lua"
        txt_file = "test.txt"
        judge.Toolkit.save(script_file, script)
        judge.Toolkit.save(txt_file, txt)
        self.judge = judge.Judge(script_file, txt_file)
        output, how_long = self.judge.run()
        self.assertEqual(output, "hello joe")
        judge.Toolkit.delete(script_file)
        judge.Toolkit.delete(txt_file)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.controller = app.Controller()
        self.py_script = '#! python\nprint(input())'
        self.py_txt = 'hello joe!'
        self.rb_script = "#! ruby\nputs(gets.chomp.to_i*2)"
        self.rb_txt = "2"
        self.rnd_script = "#! rnd\nspeak listen\n"
        self.rnd_txt = "not a real language"

    def test_can_have_a_conversation(self):
        answer = self.controller.listen(0, '/hi')
        self.assertEqual(answer, 'what?')
        answer = self.controller.listen(0, '/start')
        self.assertEqual(answer, 'script:')
        answer = self.controller.listen(1, '/start')
        self.assertEqual(answer, 'script:')
        answer = self.controller.listen(1, self.rb_script)
        self.assertEqual(answer, 'text:')
        answer = self.controller.listen(1, self.rb_txt)
        self.assertEqual(answer, '4')
        answer = self.controller.listen(0, self.py_script)
        self.assertEqual(answer, 'text:')
        answer = self.controller.listen(0, self.py_txt)
        self.assertEqual(answer, self.py_txt)

    def test_can_cancel_a_conversation(self):
        answer = self.controller.listen(1, '/start')
        self.assertEqual(answer, 'script:')
        answer = self.controller.listen(1, self.rb_script)
        self.assertEqual(answer, 'text:')
        answer = self.controller.listen(1, '/cancel')
        self.assertEqual(answer, 'ok')
        answer = self.controller.listen(1, self.rb_script)
        self.assertEqual(answer, 'what?')
        answer = self.controller.listen(1, '/start')
        self.assertEqual(answer, 'script:')

    def test_can_understand_languages(self):
        lang = self.controller.understand(self.py_script)
        self.assertEqual(lang, 'python')
        lang = self.controller.understand(self.rb_script)
        self.assertEqual(lang, 'ruby')

    def test_can_run_only_after_saving(self):
        self.controller.listen(1, '/start')
        with self.assertRaises(RuntimeError):
            self.controller.run(1)
        self.controller.listen(1, self.py_script)
        with self.assertRaises(RuntimeError):
            self.controller.run(1)
        output = self.controller.listen(1, self.py_txt)
        self.assertEqual(output, self.py_txt)

    def test_can_survive_an_unknown_language(self):
        self.controller.listen(1, '/start')
        answer = self.controller.listen(1, self.rnd_script)
        self.assertEqual(answer, "Unknown language")
        answer = self.controller.listen(1, self.rnd_txt)
        self.assertEqual(answer, 'what?')

if __name__ == '__main__':
    unittest.main()
