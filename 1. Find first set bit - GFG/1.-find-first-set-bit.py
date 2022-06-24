#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if n==0:
            return 0
        count=0
        c=n
        while n!=0:
            count+=1
            n=n//2 
        for i in range(count+1):
            D=1
            if (c>>i)&(D):
                return i+1
        return 0
            
        
        

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends