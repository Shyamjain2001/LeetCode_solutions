#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        def go(n):
            if n==1:
                print(1,end=' ')
                return
            go(n-1)
            print(n,end=' ')
        go(N)
        return 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends