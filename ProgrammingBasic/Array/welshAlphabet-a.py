alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
#sort(['abcd', 'abcdd'])
#[0,1,2,5] <-> [0,1,2,4]

def sort(words):

    alphabet_index_map = {char: idx for idx, char in enumerate(alphabets)}

    # convert words to array of indices
    word_arrays = []
    for word in words:
        word_arr = []
        idx = 0
        while idx < len(word):
            if word[idx:idx+2] in alphabet_index_map:
                word_arr.append(alphabet_index_map[word[idx:idx+2]])
                idx += 2
            else:
                word_arr.append(alphabet_index_map[word[idx:idx+1]])
                idx += 1
        word_arrays.append(word_arr)

    # sort
    word_arrays.sort()

    # convert back to words
    sorted_words = []
    for word_arr in word_arrays:
        for idx, pos in enumerate(word_arr):
            word_arr[idx] = alphabets[pos]
        sorted_words.append(''.join(word_arr))

    return sorted_words


print(sort(['abcd', 'abcdd']))
# ['abcdd', 'abcd']
print(sort(['abcd', 'abcdd', 'abcch']))
# ['abcch', 'abcdd', 'abcd']
print(sort(["d", "ddr", "nah", "dd", "dea", "ngah"]))
# ['dd', 'ddr', 'd', 'dea', 'ngah', 'nah']