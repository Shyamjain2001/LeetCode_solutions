#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        lst=[]
        if arr[0]==0 and len(arr)==1:
            return 1
        arr=list(set(arr))
        for i in arr:
            if i>0:
                lst.append(i)
        lst.sort()
        for i in range(len(lst)):
            if i+1==lst[i]:
                pass 
            else:
                return i+1
        return lst[-1]+1
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends