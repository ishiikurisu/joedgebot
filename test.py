import unittest
import judge    

class TestJudge(unittest.TestCase):
    def test_try_to_open_inexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.judge = judge.Judge('randomscript', 'randominlet')

if __name__ == '__main__':
    unittest.main()
