def isAnagram(s, t):
    a = len(s)
    if a != len(t):
        return False

    chars = [0] * 26

    for i in range(a):
        chars[ord(s[i]) - ord('a')] += 1
        chars[ord(t[i]) - ord('a')] -= 1

    for i in range(26):
        if chars[i]!=0:
            return False

    return True


print(isAnagram('nagaram','nagaram'))