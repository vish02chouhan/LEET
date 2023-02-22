def powerset(s):
    """
    Returns the powerset of a given set s.
    """
    n = len(s)
    # The total number of subsets is 2^n.
    powerset_size = 2**n
    result = []
    # Loop over all possible binary numbers of length n.
    for i in range(powerset_size):
        subset = []
        # Convert the binary number to a set.
        for j in range(n):
            if i & (1 << j):
                subset.append(s[j])
        result.append(subset)
    return result

s = [1, 2, 3]
print(powerset(s))