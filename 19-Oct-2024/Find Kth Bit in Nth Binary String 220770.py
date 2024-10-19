# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def compute(n):
            if n == 1:
                return '0'
            bef = compute(n-1)
            revert = []
            for i in bef:
                app = '1'
                if i == '1':
                    app = '0'
                revert.append(app)
            revert.reverse()

            return bef + '1' + "".join(revert)
        
        curr = compute(n)
        ans = curr[k-1]
        return ans
