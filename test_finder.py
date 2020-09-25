import unittest

from finder import Finder

class TestFinder(unittest.TestCase):

    def test_readDictionaryContents(self):
        path = "./test.txt"
        f = Finder(path)
        lines = f.readDictionaryContents(path)
        self.assertEqual(["line1", "line2", "line3"], lines)

    def test_buildMap(self):
        f = Finder("./test.txt")
        f.lines = ["dog", "cat", "god"]
        f.buildMap()

        expected = {"dgo" : ["dog", "god"], "act" : ["cat"]}
        self.assertEqual(expected, f.map)

    def test_buildMapEmpty(self):
        f = Finder("./test.txt")
        f.lines = []
        f.buildMap()

        expected = {}
        self.assertEqual(expected, f.map)

    def test_findAnagrams(self):
        f = Finder("./english.txt")
        anagrams = f.findAnagrams("yielded")

        expected = ['deedily', 'yielded'] 
        self.assertEqual(expected, anagrams)

    def test_findAnagramsEmpty(self):
        f = Finder("./english.txt")
        anagrams = f.findAnagrams("catzzzz")

        expected = [] 
        self.assertEqual(expected, anagrams)                

if __name__ == "__main__":
    unittest.main()
