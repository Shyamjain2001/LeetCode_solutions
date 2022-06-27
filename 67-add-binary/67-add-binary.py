class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a=len(a)
        len_b=len(b)
        res=''
        carry=0
        a,b=a[::-1],b[::-1]
        t=max(len_a,len_b)
        for i in range(t):
            da=a[i] if i<len_a else 0
            db=b[i] if i<len_b else 0
            da=int(da)
            db=int(db)
            total=db+da+carry
            op=str(total%2)
            res=op+res
            carry=total//2 
        if carry:
            res='1'+res
        return res
        
                    
                
            
        
        