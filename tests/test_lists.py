from unittest import TestCase
from collections import Iterable

from util_funcs import unique, non_repeat, flatten

class TestUnique(TestCase):

    def test_basic(self):
        """Test basic unique functionality"""
        l = [1, 1, 7, 7, 3, 3, 4, 5, 6]
        r = [1, 7, 3, 4, 5, 6]
        self.assertEqual(unique(l), r)
 
        l = [1, 2, 7, 3, 3, 4, 7, 5, 9, 1]
        r = [1, 2, 7, 3, 4, 5, 9]
        self.assertEqual(unique(l), r)

        l = []
        r = []
        self.assertEqual(unique(l), r)

        l = ["the", "string", "compare", "string"]
        r = ["the", "string", "compare"]
        self.assertEqual(unique(l), r)

        # List containing None Elements
        l = [1, None, 12, 1]
        r = [1, None, 12]
        self.assertEqual(unique(l), r)

        l = [1, None, 12, 4, None, 1, 4]
        r = [1, None, 12, 4]
        self.assertEqual(unique(l), r)

    def test_id_function(self):
        """"""
        l = ["ab", "cc", "fgh", "gg", "fff", "asdfs", "ff"]
        r = ["ab", "fgh", "asdfs"]
        self.assertEqual(unique(l, lambda s: len(s)), r)

        l = [(1, 2), (2, 1), (3, 1), (4, 2), (5, 3)]
        r = [(1, 2), (2, 1), (5, 3)]
        self.assertEqual(unique(l, lambda s: s[1]), r)

    def test_order_preserve(self):
        """Test order is preserved"""
        l = [4, 6, 2, 3, 4, 4, 3]
        r = [4, 6, 2, 3]
        self.assertEqual(unique(l), r)



class TestNonRepeat(TestCase):

    def test_basic(self):
        """Test basic non_repeat functionality"""
        l = [2, 4, 6, 5, 2, 5]
        r = [4, 6]
        self.assertEqual(non_repeat(l), r)

        l = ["qw", "weq", "sr", "weq", "aa"]
        r = ["qw", "sr", "aa"]
        self.assertEqual(non_repeat(l), r)

        l = []
        r = []
        self.assertEqual(unique(l), r)

        # List containing None Elements
        l = [1, None, 1, 4, 5, 4, 8]
        r = [None, 5, 8]
        self.assertEqual(non_repeat(l), r)

        l = [7, 1, None, 4, None, 1]
        r = [7, 4]
        self.assertEqual(non_repeat(l), r)

    def test_id_function(self):
        """Test custom comparison functions"""
        l = ["asdf", "a", "iiii", "fffff", "oooooo", "eeeee"]
        r = ["a", "oooooo"]
        self.assertEqual(non_repeat(l, lambda s: len(s)), r)

        l = [(1, 2), (2, 2), (3, 3), (4, 3), (5, 4)]
        r = [(5, 4)]
        self.assertEqual(non_repeat(l, lambda s: s[1]), r)



class TestFlatten(TestCase):
    """ """

    def test_default(self):
        """Test default parameters are depth=1 and ftypes=(tuple, list)"""
        # test default depth = 1
        l = [1, [2, [3, 4]], 5, [6, 7]]
        r = [1, 2, [3, 4], 5, 6, 7]
        self.assertEqual(flatten(l), r)

        # test default types are tuple and list
        d = {"a": 1}
        l = [(4, 5), d, 1, 2, 3]
        r = [(4, 5), d, 1, 2, 3]
        self.assertEqual(flatten(l, depth=22, ftypes=(list,)), r)

    def test_depth(self):
        """Test it only flattens to required depth""" 
        l = [1, [2, 3, 4], 5, [6, 7]]
        r = [1, [2, 3, 4], 5, [6, 7]]
        self.assertEqual(flatten(l, 0), r)

        l = [1, [2, 3, 4], 5, [6, 7]]
        r = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten(l, 1), r)

        l = [1, [2, 3, [4, 5]], 6, [7, 8]]
        r = [1, 2, 3, [4, 5], 6, 7, 8]
        self.assertEqual(flatten(l, 1), r)
        
        l = (1, (2, 3, [4, 5]), 6, [7, 8])
        r = [1, 2, 3, [4, 5], 6, 7, 8]
        self.assertEqual(flatten(l, 1), r)

        l = [1, [2, 3, [4, 5]], 6, [7, 8]]
        r = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(l, 2), r)

        # Test it stops when everything is flattened
        l = [1, [2, 3, 4], 5, [6, 7], [1, 2], [1, 2], [1, 2]]
        r = [1, 2, 3, 4, 5, 6, 7, 1, 2, 1, 2, 1, 2]
        self.assertEqual(flatten(l, 99999999999999), r)

    def test_types(self):
        """Test types that are flattned"""
        l = [range(1, 5), range(5, 6), range(6, 11)]
        r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(flatten(l, ftypes=(Iterable,)), r)

        l = [1, 2, (3, 5), 6, (7, (8, 9))]
        r = [1, 2, (3, 5), 6, (7, (8, 9))]
        self.assertEqual(flatten(l, ftypes=(list,)), r)

        l = ((5, 6), (9, (8, 8)), 2, 3, 4)
        r = [5, 6, 9, (8, 8), 2, 3, 4]
        self.assertEqual(flatten(l, ftypes=(tuple,)), r)
