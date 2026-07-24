class Solution:
    def climbStairs(self, n: int) -> int:
        #return nth position of fibonacci sequence
        if n <= 0:
            return [0]
        
        fib = [1, 1]
        for i in range(2, n + 1):
            # Adds the last two elements together
            fib.append(fib[-1] + fib[-2]) 
        return fib[n]
        