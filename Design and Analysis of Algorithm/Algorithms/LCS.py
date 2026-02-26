# Recursive approach (Time Complexity --> O(2^n))
def LCS_string(A,B,i,j):
    if i == 0 or j == 0:
        return 0
    
    if A[i - 1] == B[j - 1]:
        return 1 + LCS_string(A,B, i-1,j-1)

    else:
        return max(LCS_string(A,B,i-1,j),LCS_string(A,B,i,j-1))
    



# Dynamic Programming approach  (Time Complexity --> O(m*n))
def LCS(A, B):
    m = len(A)
    n = len(B)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n], dp

A = "ABCBDAB"
B = "BDCABA"

m = len(A)
n = len(B)

print("LCS length : ",LCS_string(A,B,m,n))