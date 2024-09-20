class Solution:
    def reverseBits(self,n: int) -> int:
        reversed_num = 0

        for i in range(32):
            # Get the last bit of n
            last_bit = n & 1
            # Shift reversed_num to the left to make room for the new bit
            reversed_num = (reversed_num << 1) | last_bit
            # Shift n to the right to process the next bit
            n >>= 1

        return reversed_num
