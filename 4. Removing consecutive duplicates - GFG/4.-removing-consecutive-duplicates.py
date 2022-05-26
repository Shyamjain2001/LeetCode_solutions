
#User function Template for python3

class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        # code here
        st=[]
        st.append(s[0])
        for i in s:
            if st[-1]!=i:
                st.append(i)
        op=''
        for i in st:
            op+=i 
        return op
            

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
        obj = Solution()
        print(obj.removeConsecutiveDuplicates(str(input())))
# } Driver Code Ends