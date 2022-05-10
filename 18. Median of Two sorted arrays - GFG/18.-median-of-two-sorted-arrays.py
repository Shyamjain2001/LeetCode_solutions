#User function Template for python3

class Solution:
    
    #Function to find the median of the two arrays when they get merged.

       
        #code here
    def findMedianSortedArrays(self,arr1, n1, arr2, n2):
        i=j=0
        lst=[]
        while n1>i and n2>j:
            if arr1[i]>arr2[j]:
                lst.append(arr2[j])
                j+=1
            else:
                lst.append(arr1[i])
                i+=1
        while n1>i:
            lst.append(arr1[i])
            i+=1
        while n2>j:
            lst.append(arr2[j])
            j+=1
        x=n1+n2
        #print(lst)
        if x%2==0:
            mid=x//2
            #return mid
            return (lst[mid]+lst[mid-1])//2
        else:
            return lst[x//2]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(Solution().findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(Solution().findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends