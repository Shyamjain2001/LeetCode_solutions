class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[-1][-1]<target:
            return False
        for i in matrix:
            if i[0]<=target and i[-1]>=target:
                break
        if target in i:
            return True
        return False
        