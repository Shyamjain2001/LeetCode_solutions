class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        right = len(nums) - 1
        
        if nums[right] > nums[right-1]:
            nums[right], nums[right-1] = nums[right-1], nums[right]
            return
            
        while right > 0 and nums[right] <= nums[right-1]:
            right -= 1
        
        left = right - 1
        minimum = nums[right]
        minimum_index = right
        for i in range(right, len(nums)):
            if nums[i] > nums[left] and nums[i] < minimum:
                minimum = nums[i]
                minimum_index = i
        
        nums[left], nums[minimum_index] = nums[minimum_index], nums[left]
        
        sorted_values = sorted(nums[left+1:])
        for i in range(left+1, len(nums)):  
            nums[i] = sorted_values[i-left-1]
   
                
        