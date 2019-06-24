class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        i=0
        nums.sort()
        for x in  range(0,len(nums),2):
            i= i + nums[x]
        
        return i
