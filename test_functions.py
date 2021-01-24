import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
# from io import StringIO

# def get_answer_input():
    # return input('Enter your guess: ') 

class TestFunctions(unittest.TestCase):

    # @patch("sys.stdin", StringIO("answer1\nanswer2\n"))
    def test_compare(self):
            for i in range(10):
                self.assertEqual(len(mastermind.create_code()), 4)
                code = mastermind.create_code()
                for item in code:
                    self.assertIn(item, range(1, 9))
        # self.assertEqual(get_answer_input(), "answer2te)
        # result = mastermind.create_code()
        # self.assert(result,1345)

    def test_correctness(self):
        # with patch
        correct = mastermind.check_correctness(4, 12)
        self.assertTrue(correct)
        correct = mastermind.check_correctness(2, 11)
        self.assertFalse(correct)
       
       
       
    # @patch("sys.stdin", StringIO("123\n12345\n1234\n"))
    @patch("sys.stdin", StringIO("1234\n"))
    def test_input(self):
        '''
        Must be a string with 4 digits
        Must repeat until certain conditions are met
        '''
        code = str(1234) 
        self.assertEqual(mastermind.get_answer_input(),code)
        # self.assertEqual(mastermind.get_answer_input(),code)
        # self.assertEqual(mastermind.get_answer_input(),code)


        # self.assertEqual(answer, str(answer), True)  
        # self.assertEqual(len(answer), 4, False)
        
    # def test_input(self):
    #     answer = mastermind.get_answer_input()
      
    #     answer = StringIO()
    #     with redirect_stdout(answer):
    #         test_input()
    @patch("sys.stdin", StringIO("1234\n5762\n3412"))
    def test_take_turn(self):
        # try:
        code = [1,2,3,4]
        answer = mastermind.take_turn(code,12)
        # print("answer:", end ="")
        # print(answer)
        self.assertEqual(answer, (4,0))
        # self.assertEqual(mastermind.take_turn(code,12), (0,1))
        # self.assertEqual(mastermind.take_turn(code,12), (0,4))
        # self.assertEqual(mastermind.take_turn(code), (0,4))
        # except:
        #     EOFError: "EOF when reading a line"




if __name__ == "__main__":
    unittest.main()
