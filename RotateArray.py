class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            p=nums[len(nums)-1]
            for j in range(len(nums)):
                t = nums[j]
                nums[j] = p
                p=t
        
