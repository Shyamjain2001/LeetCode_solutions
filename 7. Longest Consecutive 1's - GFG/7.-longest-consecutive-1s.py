#User function Template for python3


import math
class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        #start here
        rep=0
        x=math.log2(N)
        x=math.floor(x)+1
        count=0
        more=0
        for i in range(x+1):
            if (N>>i)&1:
                #print(i)
                count+=1
            else:
                if count>=more:
                    more=count
                count=0
        return more
                
                
                
            
            
       
            
            




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends