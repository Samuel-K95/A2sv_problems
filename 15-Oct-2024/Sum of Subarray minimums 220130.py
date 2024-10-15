# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        st = []
        for i , n in enumerate(arr):
            while st and n < st[-1][1]:
                j, m = st.pop()
                left = j - st[-1][0] if st else j + 1
                right = i - j
                ans = (ans + m * left * right) % MOD 
            st.append((i, n))

        for i in range(len(st)):
            j, n = st[i]
            left = j - st[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            ans = (ans + n * left * right) % MOD
        return ans