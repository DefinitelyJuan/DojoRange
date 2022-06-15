import unittest
from kataRange import rango

class testCases(unittest.TestCase):
    def test_Contains(self):
        self.assertEqual(rango.contains((2,True),(6,False),[2,4]),True)
    def test_Contains2(self):
        self.assertEqual(rango.contains((2,True),(6,False),[-1,1,6,10]),False)
    def test_getAll(self):
        self.assertEqual(rango.getAllPoints((2,True),(6,False)), [2,3,4,5])
    def test_Equals(self):
        self.assertEqual(rango.equals((3,True),(5,False),(3,True),(5,False)))