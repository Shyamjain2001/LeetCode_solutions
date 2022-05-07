class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr=height
        i=0
        j=len(height)-1
        if len(height)<=1:
            return 0
        old=0
        while i<j:
            new=min(arr[i],arr[j])*(j-i)
            if new>old:
                old=new
            if arr[j]>arr[i]:
                i=i+1
            else:
                j=j-1
        return old
            
            
        