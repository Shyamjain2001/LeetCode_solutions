#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        st=0
        end=len(arr)-1
        N=len(arr)
        while st<=end:
            mid=st+(end-st)//2
            if mid==0 and arr[mid]<arr[mid+1]:
                return arr[mid]
            elif mid==len(arr)-1 and arr[mid]<arr[mid-1]:
                return arr[mid]
            elif arr[mid]<arr[mid+1] and arr[mid]<arr[mid-1]:
                return arr[mid]
            elif arr[mid]>arr[end]:
                st=mid+1
            elif arr[mid]<arr[end]:
                end=mid-1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends