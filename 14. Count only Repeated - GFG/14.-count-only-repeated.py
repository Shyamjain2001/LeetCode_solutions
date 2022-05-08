#User function Template for python3

class Solution:
    
    #Function to find repeated element and its frequency.
    def findRepeating(self,arr,n):
        #code here
       if n==1:
           return (-1,-1)
       st=0
       end=n-1
       rep=-1
       while st<=end:
           mid=(st+end)//2
           if arr[mid]==arr[mid-1] and mid>1:
               rep=arr[mid]
           elif arr[mid]==arr[mid+1] and mid<n-1:
               rep=arr[mid]
           if arr[end]-arr[mid]==end-mid:
               end=mid-1
           else:
               st=mid+1
    
       if rep==-1:
           return (-1,-1)
       return (rep,len(arr)-1-(arr[n-1]-1-arr[0]))
                   
                    
            
                
                    
                
            
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = list((map(int,input().strip().split())))
        
        ans=Solution().findRepeating(arr,n)
        print(ans[0],ans[1])
        
        
# } Driver Code Ends