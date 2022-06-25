#User function Template for python3
import math
class Solution:
    ##Complete this fcuntion
    # Function to find the gray code of given number n
    def greyConverter(self,n):
        ##Your code here
        n1=n>>1
        op=n^n1
        return op

            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.greyConverter(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends