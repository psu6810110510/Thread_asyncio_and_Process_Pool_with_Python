from coe_6810110510.n2_utils import find_second_largest
import unittest

class TestSecondLargest(unittest.TestCase):
    def test_second_largest_input_1_2_3_should_be_2(self):
        self.assertEqual(find_second_largest([1, 2, 3]), 2)

    def test_second_largest_input_5_4_3_should_be_4(self):
        self.assertEqual(find_second_largest([5, 4, 3]), 4)

    def test_second_largest_input_7_7_7_should_be_None(self):
        self.assertIsNone(find_second_largest([7, 7, 7]))

    def test_second_largest_input_10_should_be_None(self):
        self.assertIsNone(find_second_largest([10]))

    def test_second_largest_input_empty_list_should_be_None(self):
        self.assertIsNone(find_second_largest([]))

    def test_second_largest_input_with_duplicates_should_be_correct(self):
        self.assertEqual(find_second_largest([1, 2, 2, 3]), 2)
        self.assertEqual(find_second_largest([5, 5, 4, 3]), 4)

    def test_second_largest_input_with_negative_numbers(self):
        self.assertEqual(find_second_largest([-1, -2, -3]), -2)
        self.assertEqual(find_second_largest([-5, -4, -3]), -4)

    def test_second_largest_input_with_string_should_raise_TypeError(self):
        self.assertRaises(TypeError, find_second_largest, ["1", "2", "3"])

    def test_second_largest_input_with_mixed_types_should_raise_TypeError(self):
        self.assertRaises(TypeError, find_second_largest, [1, "2", 3])

    def test_second_largest_input_with_all_same_numbers_should_be_None(self):
        self.assertIsNone(find_second_largest([4, 4, 4, 4]))

    def test_second_largest_input_with_special_characters_should_raise_TypeError(self):
        self.assertRaises(TypeError, find_second_largest, ["@", "#", "$"])