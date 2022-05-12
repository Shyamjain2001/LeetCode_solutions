# User function Template for python3

class Solution:
    def toh(self, N,a,b,c):
        # Your code here
        def Toh(n,a,b,c):
            if n>0:
                Toh(n-1,a,c,b)
                print('move disk',n,'from rod',a,'to rod',b)
                Toh(n-1,c,b,a)
            return
        Toh(N,a,b,c)
        return (2**N)-1
            
            

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends