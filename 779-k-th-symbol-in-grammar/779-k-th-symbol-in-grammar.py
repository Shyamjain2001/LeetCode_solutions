class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth(n,k):
            if k==1:
                return False
            if k==2 and n==2:
                return True
            mid=(2**n)//2
            if k<=mid:
                return kth(n-1,k)
            else:
                return not(kth(n-1,k-mid))
        if kth(n,k):
            return 1
        return 0
        