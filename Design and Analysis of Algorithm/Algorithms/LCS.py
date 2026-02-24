# Recursive approach (Time Complexity --> O(2^n))
def LCS_string(A,B,i,j):
    if i == 0 or j == 0:
        return 0
    
    if A[i - 1] == B[j - 1]:
        return 1 + LCS_string(A,B, i-1,j-1)

    else:
        return max(LCS_string(A,B,i-1,j),LCS_string(A,B,i,j-1))
    



# Dynamic Programming approach  (Time Complexity --> O(m*n))
from functools import lru_cache

@lru_cache(None)
def LCS_string(A,B,i, j):
    if i == 0 or j == 0:
        return 0
    if A[i-1] == B[j-1]:
        return 1 + LCS_string(A,B,i-1, j-1)
    return max(LCS_string(A,B,i-1, j), LCS_string(A,B,i, j-1))


A = "ABCBDAB"
B = "BDCABA"

m = len(A)
n = len(B)

print("LCS length : ",LCS_string(A,B,m,n))