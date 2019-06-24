class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ls=[]
        for i in range(0,len(A)):
            ls.append(pow(abs(A[i]),2))
            
        ls.sort()
        return ls
            
