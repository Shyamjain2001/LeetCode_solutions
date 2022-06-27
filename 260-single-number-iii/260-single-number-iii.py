class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for i in nums:
            x^=i 
        p=1
        while (x&1)==0:
            x>>=1
            p<<=1
        a,b=0,0
        for i in nums:
            if (i&p):
                a^=i
            else:
                b^=i 
        return a,b
                
            
        