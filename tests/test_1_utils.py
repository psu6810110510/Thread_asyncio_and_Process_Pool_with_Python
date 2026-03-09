from coe_6810110510.n1_utils import count_vowels
import unittest

class TestCountVowel(unittest.TestCase):
    def test_count_vowels_input_What_should_be_1(self):
        self.assertEqual(count_vowels("What"), 1)
    
    def test_count_vowels_input_goarOund_should_be_4(self):
        self.assertEqual(count_vowels("goarOund"), 4)
    
    def test_count_vowels_input_empty_string_should_be_0(self):
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_input_12345_should_be_0(self):
        self.assertEqual(count_vowels("12345"), 0)
    
    def test_count_vowels_input_None_should_be_TypeError(self):
        self.assertRaises(TypeError, count_vowels, None)

    def test_count_vowels_input_aeiouAEIOU_should_be_10(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_count_vowels_input_special_characters(self):
        self.assertEqual(count_vowels("W@a1"), 1)
    
    def test_count_vowels_input_drwt_should_be_0(self):
        self.assertEqual(count_vowels("drwt"), 0)
