# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st=1
        end=n
        k=-1
        while st<=end:
            mid=(st+end)//2
            if isBadVersion(mid):
                k=mid
                end=mid-1
            if not(isBadVersion(mid)):
                st=mid+1 
        return k
        
        