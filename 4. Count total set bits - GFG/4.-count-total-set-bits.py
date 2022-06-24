#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        if n==1:
            #print('termination condition >>>',1)
            return 1
        def give(n):
            no=math.log2(n)
            return math.floor(no)
        x=give(n)
        #print('this is value of x',x)
        p1=2**(x-1)*x
        p2=n-(2**x)+1
        #print('this is p1 for--',n,'>>>',p1)
        #print('this is p2 for--',n,'>>>',p2)
        if n-(2**x)==0:
            return p1+p2
        return p1+p2+self.countSetBits(n-(2**x)) 
        
            
            
            
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends