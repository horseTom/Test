import unittest
from ddt import ddt, data, unpack
from mycode import larger_than_two, has_three_elements, is_a_greeting

@ddt
class MyTest(unittest.TestCase):
    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        self.assertTrue(larger_than_two(value))

    @data([1], [0], [-3], [2])
    @unpack
    def test_no_larger_than_two(self, value):
        self.assertFalse(larger_than_two(value))