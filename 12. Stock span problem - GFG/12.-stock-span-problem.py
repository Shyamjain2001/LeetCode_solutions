#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        lst=a
        vect,stk=[],[]
        for i in range(n):
            if len(stk)==0:
                vect.append(-1)
                stk.append([lst[i],i])
            elif stk[-1][0]>lst[i]:
                vect.append(stk[-1][1])
                stk.append([lst[i],i])
            else:
                while len(stk)>=0:
                    if len(stk)==0:
                        vect.append(-1)
                        stk.append([lst[i],i])
                        break 
                    k=stk.pop()
                    if k[0]>lst[i]:
                        vect.append(k[1])
                        stk.append(k)
                        stk.append([lst[i],i])
                        break 
        op=[]
        for i in range(len(vect)):
            k=i-vect[i]
            op.append(k)
        return op
                    
                    
                    
                
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

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
        ans = obj.calculateSpan(a, n);
        for i in range(n):
            print(ans[i],end=" ")
        print()            
# } Driver Code Ends