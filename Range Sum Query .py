x=[]
class NumArray:
    def __init__(self, nums: List[int]): 
        for i in range(0,len(nums)):
            x.append(nums[i])

    def sumRange(self, i: int, j: int) -> int:
        sum=0
        if(i==j):
                    sum +=x[i]
        elif(i!=j):
                  for k in range(i,j+1):
                                        sum += x[k]
                  
        return sum
            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
