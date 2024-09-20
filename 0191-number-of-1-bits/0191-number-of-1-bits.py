class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            count += n & 1  # Increment count if the last bit is 1
            n >>= 1  # Shift right to check the next bit
        
        return count

            