def patternMatcher(pattern, string):
    # Write your code here.
    pass


pattern = "xxyxxy"

matcher = "gogopowerrangergogopowerranger"

patternDictionary = {}
for item in pattern:
    if item in patternDictionary:
        patternDictionary[item] += 1
    else:
        patternDictionary[item] = 1

probableWords = {}
for key in patternDictionary:
    keyCount = patternDictionary[key]
    for i in range(len(matcher)):
        for j in range(i, len(matcher)):
            word = matcher[i:j+1]
            wordCount = matcher.count(word)
            if wordCount == keyCount:
                probableWords.add(word)    

print(probableWords)

