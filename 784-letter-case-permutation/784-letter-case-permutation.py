class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        op=''
        def go(s,op,res):
            num=['1','2','3','4','5','6','7','8','9','0']
            if len(s)==0:
                res.append(op)
                return 
            elif s[0] not in num:
                k=s[0].lower()
                op1=op+k
                op2=op+k.upper()
                print(op1)
                print(op2)
                go(s[1:],op1,res)
                go(s[1:],op2,res)
            elif s[0] in num:
                op+=s[0]
                go(s[1:],op,res)
        go(s,op,res)
        return res
        
        
        