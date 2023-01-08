# def wordPattern(pattern, word_str):

#     words = word_str.split(" ")
#     if len(pattern) != len(words):
#         return False

#     # use two dictionaries, mapping character / string with index
#     pattern_map, word_map = {}, {}
#     for i in range(len(pattern)):
#         if pattern_map.get(pattern[i],-1)!= word_map.get(words[i],-1):
#             return False
#         pattern_map[pattern[i]] = word_map[words[i]] = i

#     return True

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    
    patternWordMapping = {}
    wordPatternMapping = {}

    for idx,item in enumerate(pattern):
        if item not in patternWordMapping:
            patternWordMapping[item] =  words[idx]
        else:
            if patternWordMapping[item] != words[idx]:
                return False

    for idx,item in enumerate(words):
        if item not in wordPatternMapping:
            wordPatternMapping[item] =  pattern[idx]
        else:
            if wordPatternMapping[item] != pattern[idx]:
                return False

            

    
    left = 0
    right = len(pattern) - 1

    while left < right:
        if pattern[left] == pattern[right] and words[left] != words[right]:
            return False

        if pattern[left] != pattern[right] and words[left] == words[right]:
            return False

        if patternWordMapping[pattern[left]] !=  words[left]:
            return False

        if patternWordMapping[pattern[right]] !=  words[right]:
            return False

        
        left += 1
        right -= 1

    return True


pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))