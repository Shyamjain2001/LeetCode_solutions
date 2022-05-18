#User function Template for python3

class Solution:
    def isLucky(self, n):
        i=2
        def go(n,i):
            #print(n,i)
            if n==i:
                return False
            elif n%i==0:
                return False
            elif n<i:
                return True
            else:
                return go(n-(n//i),i+1)
        return go(n,i)
        
      
            
                
                
                
            
        
            
           
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends