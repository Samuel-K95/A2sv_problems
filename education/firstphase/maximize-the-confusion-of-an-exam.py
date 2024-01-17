class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        check = defaultdict(int)
        ans = 0
        for right in range(len(answerKey)):
            check[answerKey[right]] += 1
            if len(check) == 2:
                while left < len(answerKey) and min(check.values()) > k:
                    check[answerKey[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans