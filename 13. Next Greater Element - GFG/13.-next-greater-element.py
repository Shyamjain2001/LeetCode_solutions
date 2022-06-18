#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        lst=arr
        vect=[]
        stk=[]
        n=len(lst)
        for i in range(n-1,-1,-1):
            if stk==[]:
                vect.append(-1)
                stk.append(lst[i])
            elif stk[-1]>=lst[i]:
                vect.append(stk[-1])
                stk.append(lst[i])
            else:
                while len(stk)>=0:
                    if len(stk)==0:
                        vect.append(-1)
                        stk.append(lst[i])
                        break
                    t=stk.pop()
                    if t>=lst[i]:
                        vect.append(t)
                        stk.append(t)
                        stk.append(lst[i])
                        break
        k=[]
        for i in range(n-1,-1,-1):
            k.append(vect[i])
        return k 
                        
                        
                    
                
            
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends