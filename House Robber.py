class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            if len(nums)==0:
                return 0
            else:
                return nums[0]
            
         
        dp=[nums[0],max(nums[1],nums[0])]
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
            
        return dp[len(nums)-1]
            
