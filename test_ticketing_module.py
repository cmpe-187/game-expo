__author__ = "Zelin Cai, Patrick Silvestre"
__license__ = "MIT"

from ticketing_module import *
import unittest

class testInvalidValues(unittest.TestCase):
    def test1(self):
        actual_output = ticketing_module(10, "none")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

class testBoy(unittest.TestCase):
    def test1(self):
        actual_output = ticketing_module(5, "boy")
        expected_output = "rhyming"
        self.assertEqual(actual_output, expected_output)

    def test2(self):
        actual_output = ticketing_module(6, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        actual_output = ticketing_module(7, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test4(self):
        actual_output = ticketing_module(9, "boy")
        expected_output = "storytelling"
        self.assertEqual(actual_output, expected_output)

    def test5(self):
        actual_output = ticketing_module(10, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test6(self):
        actual_output = ticketing_module(11, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test7(self):
        actual_output = ticketing_module(13, "boy")
        expected_output = "quiz"
        self.assertEqual(actual_output, expected_output)

    def test8(self):
        actual_output = ticketing_module(15, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test9(self):
        actual_output = ticketing_module(20, "boy")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test10(self):
        actual_output = ticketing_module(22, "boy")
        expected_output = "poetry"
        self.assertEqual(actual_output, expected_output)


class testGirl(unittest.TestCase):
    def test1(self):
        actual_output = ticketing_module(5, "girl")
        expected_output = "rhyming"
        self.assertEqual(actual_output, expected_output)

    def test2(self):
        actual_output = ticketing_module(6, "girl")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        actual_output = ticketing_module(7, "girl")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test4(self):
        actual_output = ticketing_module(9, "girl")
        expected_output = "drawing"
        self.assertEqual(actual_output, expected_output)

    def test5(self):
        actual_output = ticketing_module(10, "girl")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test6(self):
        actual_output = ticketing_module(13, "girl")
        expected_output = "essay writing"
        self.assertEqual(actual_output, expected_output)

    def test7(self):
        actual_output = ticketing_module(15, "girl")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test8(self):
        actual_output = ticketing_module(20, "girl")
        expected_output = ""
        self.assertEqual(actual_output, expected_output)

    def test9(self):
        actual_output = ticketing_module(22, "girl")
        expected_output = "poetry"
        self.assertEqual(actual_output, expected_output)