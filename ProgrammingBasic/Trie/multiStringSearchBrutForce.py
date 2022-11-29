



class ModifiedSuffixTrie:
    def __init__(self, string) -> None:
        self.root = {}
        self.endSymbol = '*'
        self.pouplateSufixTrieFrom(string)


    def pouplateSufixTrieFrom(self, string):
        for idx in range(len(string)):
            self.insertSubstringStartingAt(idx, string)


    def insertSubstringStartingAt(self,i, string):
        node = self.root
        for idx in range(i, len(string)):
            character = string[idx]
            if character not in node:
                node[character] = {}
            node = node[character]
        
        node[self.endSymbol] = '*'

    def contains(self, string):
        node = self.root
        for item in string:
            if item not in node:
                return False
            
            node= node[item]

        
        return True


bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]



def multiStringSearch(bigString, smallStrings):
        suffix = ModifiedSuffixTrie(bigString)
        return [ suffix.contains(string) for string in smallStrings]


print(multiStringSearch(bigString, smallStrings))