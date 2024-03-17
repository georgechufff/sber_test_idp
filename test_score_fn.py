import unittest
from score_fn import score_fn

class TestScoreFn(unittest.TestCase):

    def test_type(self):
        self.assertRaises(TypeError, score_fn, [1], [2])
        self.assertRaises(TypeError, score_fn, 1, 2)
        self.assertRaises(TypeError, score_fn, ('1', '2'))

    def test_value(self):
        self.assertRaises(ValueError, score_fn, 'ru-1001\n', 'ru-1002\n')
        self.assertRaises(ValueError, score_fn, 'ru-1001\n', 'ru-1001\n')