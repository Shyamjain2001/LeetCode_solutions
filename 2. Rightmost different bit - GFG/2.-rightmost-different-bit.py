#{ 
#Driver Code Starts
#Initial Template for Python 3

import math




    
 # } Driver Code Ends
#User function Template for python3
import math
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        posit=0
        while ((m>>posit)&1)==((n>>posit)&1):
            if posit>math.log2(max(m,n))+1:
                return -1
            posit+=1
        return posit+1
            
        

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends