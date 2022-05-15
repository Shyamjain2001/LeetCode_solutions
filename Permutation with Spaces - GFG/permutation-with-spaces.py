#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        op=str(S[0])
        res=[]
        s=S[1:]
        def go(s,res,op):
            if len(s)==0:
                res.append(op)
                return
            k=str(s[0])
            op1=op+' '+k
            op2=op+k
            #print(op1,op2)
            go(s[1:],res,op1)
            go(s[1:],res,op2)
        go(s,res,op)
        return res
                
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends