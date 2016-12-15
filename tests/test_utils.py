from unittest import TestCase

from util_funcs.lists import unique, non_repeat

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

