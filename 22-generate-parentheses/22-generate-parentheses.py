class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op='('
        opn=n-1
        clse=n
        res=[]
        def go(opn,clse,op,res):
            if clse==0:
                res.append(op)
                return 
            elif opn!=0:
                op1=op+'('
                go(opn-1,clse,op1,res)
                if opn!=clse:
                    op2=op+')'
                    go(opn,clse-1,op2,res)
            elif opn==0:
                op+=')'
                go(opn,clse-1,op,res)
        go(opn,clse,op,res)
        return res
        
        