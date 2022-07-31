import sys

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        cnt1,cnt2 = 0,0
        first,second = sys.maxsize,sys.maxsize
        
        for i in range(len(nums)):
            if first == nums[i]:
                cnt1 += 1
            elif second == nums[i]:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 += 1
                first = nums[i]
            elif cnt2 == 0:
                cnt2 += 1
                second = nums[i]
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(nums)):
            if nums[i] == first:
                cnt1 += 1
            elif nums[i] == second:
                cnt2 += 1
            
        if cnt1 > len(nums)/3:
            result.append(first)
        if cnt2 > len(nums)/3:
            result.append(second)
        
        return result
        