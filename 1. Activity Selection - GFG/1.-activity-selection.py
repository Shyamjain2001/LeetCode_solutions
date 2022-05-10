#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        newl=[]
        for i in range(len(end)):
            newl.append((start[i],end[i]))
        # now do sorting according to the ending element 
        newl=sorted(newl,key=lambda x:x[1])
        count=1
        k=newl[0]
        #print(k)
        for i in range(1,n):
            if k[1]<newl[i][0]:
                #print(newl[i])
                count+=1
                k=newl[i]
        return count
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends