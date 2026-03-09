from FizzBuzz import FizzBuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_input_is_3_should_be_Fizz(self):
        self.assertEqual(FizzBuzz(3),"Fizz")

    def test_input_is_9_should_be_Fizz(self):
        self.assertEqual(FizzBuzz(9),"Fizz")

    def test_input_is_5_should_be_Buzz(self):
        self.assertEqual(FizzBuzz(5),"Buzz")

    def test_input_is_10_should_be_Buzz(self):
        self.assertEqual(FizzBuzz(10),"Buzz")

    def test_input_is_7_should_be_None(self):
        self.assertIsNone(FizzBuzz(7))

    def test_input_is_16_should_be_None(self):
        self.assertIsNone(FizzBuzz(16))

    def test_input_is_15_should_be_FizzBuzz(self):
        self.assertEqual(FizzBuzz(15),"FizzBuzz")

    def test_input_is_45_should_be_FizzBuzz(self):
        self.assertEqual(FizzBuzz(45),"FizzBuzz")
        
    def test_input_is_3_5_should_be_not_be_Fizz(self):
        self.assertNotEqual(FizzBuzz(3.5),"Fizz")

    def test_input_is_5_3_should_be_not_be_Buzz(self):
        self.assertNotEqual(FizzBuzz(5.3),"Buzz")

    def test_input_is_0_should_be_FizzBuzz(self):
        self.assertEqual(FizzBuzz(0),"FizzBuzz")
    
    def test_input_is_negative_3_should_be_Fizz(self):
        self.assertEqual(FizzBuzz(-3),"Fizz")
    
    def test_input_is_negative_5_should_be_Buzz(self):
        self.assertEqual(FizzBuzz(-5),"Buzz")

    def test_input_is_negative_15_should_be_FizzBuzz(self):
        self.assertEqual(FizzBuzz(-15),"FizzBuzz")