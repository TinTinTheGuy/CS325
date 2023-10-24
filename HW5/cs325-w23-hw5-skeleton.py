import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2, ci = 1, cd = 1, cm = 1):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        ci: The cost of an insertion (1 by default).
        cd: The cost of a deletion (1 by default).
        cm: The cost of a mutation (1 by default).
    
    Returns:
        The edit distance between s1 and s2.
    """
    n = len(s1)
    m = len(s2)
    
    if m == 0:
        return n
    elif n == 0:
        return m
    
    Edit = [[ 0 for X in range ( m + 1 )] for X in range ( n + 1)]
    
    for i in range(0, m + 1):
        Edit[0][i] = i
    
    for i in range(0, n + 1):
        Edit[i][0] = i
    
    for i in range(1, n + 1 ):
        for j in range(1, m + 1):   
            if s1[i - 1] == s2[j - 1]:
                Edit[i][j] = Edit[i-1][j-1]
            else:
                Edit[i][j] = min(Edit[i - 1][j] + ci, 
                Edit[i][j - 1] + cd,
                Edit[i-1][j - 1] + cm)
                         
    
    # TODO: Implement this function!
    return Edit[n][m]
  

def lcs(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """
    n = len(s1)
    m = len(s2)
    
    LCS = [[ 0 for x in range ( m + 1 )] for x in range ( n + 1)]
    for i in range( n + 1):
        for j in range( m + 1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                LCS[i][j] = LCS [i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i][j - 1 ], LCS[i - 1][j])
    return LCS[n][m]
    
def lcs3(s1, s2, s3):
    """
    Computes the length of the longest common subsequence between three strings: s1, s2, and s3.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The third string.`
    
    Returns:
        The length of the longest common subsequence between s1, s2, and s3.
    """
    n = len(s1)
    m = len(s2)
    s = len(s3)
    NMS = [[[0 for x in range(s + 1)] for x in range (m + 1) ] for x in range(n + 1 )]
    for i in range( n + 1):
        for j in range ( m + 1 ):
            for k in range ( s + 1):
                if i == 0 or j == 0 or k == 0:
                    NMS[i][j][k] = 0
                
                elif s1[i - 1] == s2[ j -1 ] == s3[k - 1]:
                    NMS[i][j][k] = NMS[i - 1][j - 1][k - 1] + 1
                else:
                    NMS[i][j][k] =  max(NMS[i][j - 1][k], NMS[i - 1][j][k], NMS[i][j][k - 1])
    return NMS[n][m][s]

s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
print(edit_distance(s1, s2))
print(lcs(s1, s2))