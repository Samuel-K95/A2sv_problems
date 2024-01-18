class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # return max(sum(cardPoints[:k]), sum(cardPoints[-k:]))
        wind = len(cardPoints) - k
        left = 0
        tot = sum(cardPoints)
        curr_sum = 0
        ans = 0
        store = defaultdict(int)
        for right in range(len(cardPoints)):
            store[cardPoints[right]] += 1
            curr_sum += cardPoints[right]
            if right - left + 1 == wind:
                ans = max(ans, tot - curr_sum)
                curr_sum -= cardPoints[left]
                store[cardPoints[left]] -= 1
                left += 1
        return ans if ans != 0 else tot