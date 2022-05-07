class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lst=[]
        arr=nums
        if arr[0]<1 and len(arr)==1:
            return 1
        arr=list(set(arr))
        for i in arr:
            if i>0:
                lst.append(i)
        lst.sort()
        if len(lst)==0:
            return 1
        for i in range(len(lst)):
            if i+1==lst[i]:
                pass 
            else:
                return i+1
        return lst[-1]+1