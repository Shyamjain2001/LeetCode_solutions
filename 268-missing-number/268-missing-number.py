class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lst=sorted(nums)
        mx=max(lst)
        for i in range(mx):
            if i!=lst[i]:
                return i 
        return mx+1
        