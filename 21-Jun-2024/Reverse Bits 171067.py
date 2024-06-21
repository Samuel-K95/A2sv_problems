# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        rev = [i for i in str(bin(n))[2:]]
        rev.reverse()
        rev += ['0'] * (32 - len(rev))
        return int("".join(rev), 2)