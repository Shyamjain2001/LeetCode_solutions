class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = []
        for i in arr:
            if arr.count(i) == i:
                ans.append(i)
        return max(ans) if ans else -1