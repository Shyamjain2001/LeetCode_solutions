
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op,res=[],[]
        def go(nums,op,res):
            if len(nums)==0:
                res.append(op)
                return
            op1=copy.deepcopy(op)
            op2=copy.deepcopy(op) 
            op1.append(nums[0])
            
            #print(op1)
            #print(op2)
            #print(nums)
            go(nums[1:],op2,res)
            go(nums[1:],op1,res)
        go(nums,op,res)
        return res
        