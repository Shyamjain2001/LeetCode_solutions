class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=0
        maxi=nums[0]
        for i in nums:
            sm+=i
            if sm>maxi:
                maxi=sm 
            if sm<0:
                sm=0
        return maxi
        
        