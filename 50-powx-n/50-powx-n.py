class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ## Iterative O(log n) time and space complexity
        exp = abs(n)
        rollingSum = 1
        
        # We find the binary of n, and 
        exp_binary = bin(exp)[2:]
        len_binary = len(exp_binary)
    
        # Generate and array x**1, x**2, x**4, ...
        powersArray = [x] * len_binary    
        for i in range(1, len_binary):
            powersArray[i] = powersArray[i-1] * powersArray[i-1]
        
        # If there is a '1' in the binary, that means that power should be multiplied
        for i in range(len_binary):
            if exp_binary[i] == '1':
                rollingSum *= powersArray[len_binary-1-i]
        
        return 1/rollingSum if n < 0 else rollingSum
		