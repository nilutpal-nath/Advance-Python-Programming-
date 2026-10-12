# Longest Common Subsequence (LCS)
# Experiment 5 Based on the dynamic programming pseudocode and instructions

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence.
    lcs_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the table in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Code to reconstruct the LCS string from the table
    index = lcs_table[m][n]
    lcs_chars = [""] * index
    
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_chars), lcs_table[m][n]


# Main Program
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    subsequence, length = lcs(X, Y)
    print(f"Sequence 1: {X}")
    print(f"Sequence 2: {Y}")
    print(f"Longest Common Subsequence: {subsequence}")
    print(f"Length of LCS: {length}")