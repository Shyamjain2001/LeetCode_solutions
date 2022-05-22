#User function Template for python3


class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        res=[]
        i=0
        op=''
        df={2:['abc'],3:['def'],4:['ghi'],5:['jkl'],6:['mno'],7:['pqrs'],8:['tuv'],9:['wxyz']}
        def go(a,N,res,op,df,i):
            if len(op)==N:
                res.append(op)
                return 
            op1=op+df[a[i]][0][0]
            op2=op+df[a[i]][0][1]
            op3=op+df[a[i]][0][2]
            '''if len(df[a[i]][0])==4:
                op4=op+df[a[i]][0][3]
                go(a,N,res,op4,df,i+1)'''
                
            go(a,N,res,op1,df,i+1)
            go(a,N,res,op2,df,i+1)
            go(a,N,res,op3,df,i+1)
            if len(df[a[i]][0])==4:
                op4=op+df[a[i]][0][3]
                go(a,N,res,op4,df,i+1)
            return 
        go(a,N,res,op,df,i)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends