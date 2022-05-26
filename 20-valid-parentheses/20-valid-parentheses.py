class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2!=0:
            return False
        
        new_len=0
        str_len=len(s)
        while new_len<str_len:
            str_len=len(s)
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
            new_len=len(s)
       
        if len(s)==0:
            return True
        return False
        