#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        lst=[]
        st=''
        if 9*n<s:
            return -1
        for i in range(n):
            lst.append(9)
        for i in lst:
            if s>i:
                st+='9'
                s-=9
            else:
                val=str(s)
                st+=val
                s=0
        
        return st
        # code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends