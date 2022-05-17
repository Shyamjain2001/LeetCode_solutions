class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def go(n,k):
            if n==1:
                return n
            return (go(n-1,k)+(k-1))%n+1
        return go(n,k)