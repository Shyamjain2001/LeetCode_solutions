import copy
class Solution(object):
    def solver_helper(self,input, output,result):
        if (len(input)==0):
            #at leaf node append to output
            result.append(output)
            return

        op1=copy.deepcopy(output)
        op2=copy.deepcopy(output)
        op2.append(input[0])
        self.solver_helper(input[1:],op1,result)
        self.solver_helper(input[1:],op2,result)
            
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
               
            
        input=nums
        result,output=[],[]
        self.solver_helper(input, output,result)
        print(result)
        return result