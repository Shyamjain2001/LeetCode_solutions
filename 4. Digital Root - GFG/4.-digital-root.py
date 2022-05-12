#User function Template for python3

class Solution:
    def digitalRoot(self, n):
        '''
        :param n: given number 
        :return: digital root as defined
        '''
        # code here
        def gone(n):
            sum=0
            def go(n,sum):
                if n==0:
                    return sum
                last=n%10
                sum+=last
                n=n//10
                k=go(n,sum)
                return k
            k=go(n,sum)
            if k>9:
                return gone(k)
            else:
                return k
            
        alfa=gone(n)
        return alfa
        
        

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
        n = int(input())
        print(Solution().digitalRoot(n))
# } Driver Code Ends