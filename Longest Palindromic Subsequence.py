'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example 1-
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb"
-------------------------------------------------------------------------------
Example 2-
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        X=s
        Y=s[::-1]
        m=len(X)
        n=len(Y)
        L = [[None]*(n+1) for i in range(m+1)]
        for i in range(m+1):
                            for j in range(n+1):
                                                if i==0 or j==0:
                                                                L[i][j]=0
                                                elif X[i-1] == Y[j-1]: 
                                                                        L[i][j] = L[i-1][j-1]+1
                                                else: 
                                                        L[i][j] = max(L[i-1][j] , L[i][j-1])
        return L[m][n]
