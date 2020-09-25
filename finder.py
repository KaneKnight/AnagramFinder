class Finder:

    def __init__(self, path):
        self.lines = self.readDictionaryContents(path)
        self.buildMap()


    def readDictionaryContents(self, path):
        with open(path, "r") as f:
            return f.read().splitlines()

    def buildMap(self):
        self.map = {}
        for line in self.lines:
            sortedWord = "".join(sorted(line))
            if sortedWord not in self.map:
                self.map[sortedWord] = [line]
            else:
                self.map[sortedWord].append(line)

    def findAnagrams(self, word):
        sortedWord = "".join(sorted(word))
        if sortedWord not in self.map:
            return []
        else:
            return self.map[sortedWord]