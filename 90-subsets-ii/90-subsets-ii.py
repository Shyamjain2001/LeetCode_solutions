import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op,res=[],[]
        def go(nums,op,res):
            if len(nums)==0:
                if op not in res:
                    res.append(op)
                return 
            op1=copy.deepcopy(op)
            op2=copy.deepcopy(op)
            op1.append(nums[0])
            go(nums[1:],op1,res)
            go(nums[1:],op2,res)
            
        go(nums,op,res)
        return res