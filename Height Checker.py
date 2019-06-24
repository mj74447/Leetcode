class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        :type heights: List[int]
        :rtype: int
        """
        count=0
        p=heights
        ls=[]
        for i in range(0,len(p)):
                ls.append(p[i])    
        ls.sort()
        for i in range(0,len(p)):
          if  p[i]!=ls[i]:
                                count=count+1
        return count
        
                
                
            
        
