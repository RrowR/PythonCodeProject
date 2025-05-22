import unittest
from testedCodes.TestMyCode import my_code


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEquals(my_code(5, 3), 8)
    def test_positive_with_depositive(self):
        self.assertEquals(my_code(4, 5), 9)
