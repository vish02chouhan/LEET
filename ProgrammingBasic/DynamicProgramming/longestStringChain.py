
def longestStringChain(strings):
    sortedStrings = sorted(strings, key=len, reverse = True)
    wordSet = set(sortedStrings)
    chainDict = {}
    cache ={}
    for word in sortedStrings:
        if word not in cache:
            helper(word, wordSet, chainDict,0, cache)
        else:
            chainDict[word] = cache[word][0]


    current = 9

    return chainDict
						
def helper(word,wordSet, chainDict,length, cache):
    print(chainDict)
    print(word)
    node = {}
    chainDict[word] = node
    for idx in range(len(word)):
        currentWord = word[:idx] + word[idx+1:]
        if currentWord in wordSet:
            result = helper(currentWord, wordSet, node, length + 1, cache)
            print(word)
            cache[word] = (chainDict[word],result)
				
    return length

array = ["abcde", "bcde", "acde","abde", "cde", "de"]


longestStringChain(array)