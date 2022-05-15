class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        mn=nums[0]
        for i in range(len(nums)-1,0,-1):
            val=nums[i]+count
            diff=val-mn
            count+=diff
            mn=val
        return count
            
                
            
                
                    
                    
        