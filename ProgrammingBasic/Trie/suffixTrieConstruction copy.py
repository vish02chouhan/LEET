class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.populateSuffixTrieFrom(string)


    def populateSuffixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insetSufffixTrieAt(string[idx:])

        pass




    def insetSufffixTrieAt(self, string):
        node = self.root
        for item in string:

            if item not in node:
                node[item] = {}

            node = node[item]

        
        node[self.endSymbol] = True


    def contains(self, subString):
        node = self.root
        for item in subString:
            if item not in node:
                return False
            
            node = node[item]
        
        if node[self.endSymbol]:
            return True

        return False



suffixTrie = SuffixTrie('babc')

print(suffixTrie.contains('abc'))
            