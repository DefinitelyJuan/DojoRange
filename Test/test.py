import unittest
from kataRange import rango

class testCases(unittest.TestCase):
    def test_Contains(self):
        self.assertEqual(rango.contains((2,True),(6,False),2,4),True)
