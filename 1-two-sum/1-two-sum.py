class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=sorted(nums)
        i=0
        j=len(nums)-1
        st,end=-1,-1
        while i<=j:
            if k[i]+k[j]==target:
                st=k[i]
                end=k[j]
                break
            if k[i]+k[j]>target:
                j-=1
            if k[i]+k[j]<target:
                i+=1
        lst=[]
        for i in range(len(nums)):
            if nums[i]==st or nums[i]==end:
                lst.append(i)
        return lst
                
            
        