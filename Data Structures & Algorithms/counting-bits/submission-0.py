class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            ans.append(self.countOnes(i))

        return ans
    
    def countOnes(self, n: int) -> int:
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count

        