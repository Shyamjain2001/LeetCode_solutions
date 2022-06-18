# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        lst=a
        vect=[]
        stk=[]
        for i in range(0,n):
            if stk==[]:
                vect.append(-1)
                stk.append(lst[i])
            elif lst[i]>stk[-1]:
                vect.append(stk[-1])
                stk.append(lst[i])
            else:
                while len(stk)>=0:
                    if len(stk)==0:
                        vect.append(-1)
                        stk.append(lst[i])
                        break
                    t=stk.pop()
                    if lst[i]>t:
                        vect.append(t)
                        stk.append(t)
                        stk.append(lst[i])
                        break 
        return vect
                

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends