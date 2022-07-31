class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=0
        count=0
        for i in nums:
            if count==0:
                ele=i
            if ele==i:
                count+=1
            if ele!=i:
                count-=1
        return ele
        