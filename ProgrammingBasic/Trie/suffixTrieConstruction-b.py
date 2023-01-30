# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.preparesubString(i, string)
    
    def preparesubString(self, index, string):
        node = self.root
        for c in range(index, len(string)):
            letter = string[c]

            if letter in node:
                node = node[letter]
            else:
                node[letter] = {}
                node = node[letter]
        
        node["*"] = True



    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        
        return True if '*' in node  else False


suffixTrie = SuffixTrie('babc')

deb = 9
