#User function Template for python3


#Function to return the lexicographically sorted power-set of the string.
def powerSet(s):
    
    op=''
    res=[]
    def go(s,op,res):
        if len(s)==0:
            res.append(op)
            return
        op1=op
        op2=op
        op2+=s[0]
        go(s[1:],op1,res)
        go(s[1:],op2,res)
        return 
    go(s,op,res)
    return res
    #code here
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

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
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
# } Driver Code Ends