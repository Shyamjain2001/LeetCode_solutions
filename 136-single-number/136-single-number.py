class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=nums[0]
        op=0
        if len(nums)==1: return a
        for i in range(1,len(nums)):
            a=a^nums[i]
        return a
            
        