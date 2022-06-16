import unittest
from kataRange import rango

class testCases(unittest.TestCase):
    def test_Contains(self):
        self.assertEqual(rango.contains((2,True),(6,False),[2,4]),True)
        self.assertEqual(rango.contains((2,True),(6,False),[-1,1,6,10]),False)    
    def test_getAll(self):
        self.assertEqual(rango.getAllPoints((2,True),(6,False)), [2,3,4,5])
    def test_Equals(self):
        self.assertEqual(rango.equals((3,True),(5,False),(3,True),(5,False) ),True)
        self.assertEqual(rango.equals((2,True),(10,False),(3,True),(5,False) ),False)
        self.assertEqual(rango.equals((2,True),(5,False),(3,True),(10,False) ),False)
        self.assertEqual(rango.equals((3,True),(5,False),(2,True),(10,False) ),False)

    def test_endPoints(self):
        self.assertEqual(rango.endpoints((2,True),(6,False)), (2,5))
        self.assertEqual(rango.endpoints((2,True),(6,True)), (2,6))
        self.assertEqual(rango.endpoints((2,False),(6,False)), (3,5))
        self.assertEqual(rango.endpoints((2,False),(6,True)), (3,6))

    def test_containsRange(self):
        self.assertEqual(rango.containsRange((2,True),(5,False),[7,True],[10,False]), False)
        self.assertEqual(rango.containsRange((2,True),(5,False),[3,True],[10,False]), False)
        self.assertEqual(rango.containsRange((3,True),(5,False),[2,True],[10,False]), False)
        self.assertEqual(rango.containsRange((2,True),(10,False),[3,True],[5,True]), True)
        self.assertEqual(rango.containsRange((3,True),(5,True),[3,True],[5,True]), True)
    def test_overlapsRange(self):
        self.assertEqual(rango.overlapsRange([2,True],[5,False],[7,True],[10,False]), False)
        self.assertEqual(rango.overlapsRange([2,True],[10,False],[3,True],[5,False]), True)
        self.assertEqual(rango.overlapsRange([3,True],[5,False],[3,True],[5,False]), True)
        self.assertEqual(rango.overlapsRange([2,True],[5,False],[3,True],[10,False]), True)
        self.assertEqual(rango.overlapsRange([3,True],[5,False],[2,True],[10,False]), True)
