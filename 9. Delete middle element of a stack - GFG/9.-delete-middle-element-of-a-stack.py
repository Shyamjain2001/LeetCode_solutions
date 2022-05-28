#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        st=[]
        n=sizeOfStack
        if n<=1:
            return st 
        mid=n//2
        if n%2!=0:
            s.pop(mid)
        else:
            s.pop(mid-1)
        for i in range(len(s)-1,0,-1):
            st.append(s[i])
        return st
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends