#User function Template for python3

class Solution:
    def RecursivePower(self,n,p):
        '''
        return value of n^p recursively;
        '''
        # code here
        if p==0:
            return 1
        i=0
        k=n
        def go(n,k,p,i):
            if i+1==p:
                return n
            #print(i)
            n=n*k
            i+=1
            return go(n,k,p,i)
        return go(n,k,p,i)
            

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
        n,p = map(int,input().strip().split())
        print(Solution().RecursivePower(n,p))
# } Driver Code Ends