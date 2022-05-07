#{ 
#Driver Code Starts
#Initial Template for Python 3


# Python3 implementation of the approach 


 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return the maximum water that can be stored.
    def maxWater(self, height, n): 
        #Your code here
        arr=height
        if n<=2:
            return 0
        i=0
        j=n-1
        stored=0
        while i<j:
            new_stored=min(arr[i],arr[j])*(j-i-1)
            if new_stored>=stored:
                stored=new_stored
            if arr[i]<arr[j]:
                i=i+1
            else:
                j=j-1 
        return stored
                
     

#{ 
#Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        height=[int(x) for x in input().strip().split()]
        ob=Solution()
        print (ob.maxWater(height, n));
        t-=1

if __name__ == "__main__":
    main()
#} Driver Code Ends