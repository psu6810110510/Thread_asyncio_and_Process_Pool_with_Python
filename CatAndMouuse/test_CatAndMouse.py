from CatAndMouse import cat_and_mouse
import unittest

class CatAndMouseTestCase(unittest.TestCase):
    def test_cat_and_mouse_input_1_2_3_should_be_Cat_B(self):
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")
        self.assertEqual(cat_and_mouse(1, 5,7 ), "Cat B")
        
    def test_cat_and_mouse_input_1_5_2_should_be_Cat_A(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")
        self.assertEqual(cat_and_mouse(2, 5, 3), "Cat A")

    def test_cat_and_mouse_input_2_4_3_should_be_Mouse_C(self):
        self.assertEqual(cat_and_mouse(2, 4, 3), "Mouse C")
        self.assertEqual(cat_and_mouse(2, 6, 4), "Mouse C")

    def test_cat_and_mouse_input_0_5_2_should_be_assertion_error(self): 
        self.assertRaises(AssertionError,cat_and_mouse, 101, 5, 1)
        self.assertRaises(AssertionError,cat_and_mouse, -1, 5, 1)