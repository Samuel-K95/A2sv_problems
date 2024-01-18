class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        left = 0
        store = defaultdict(int)
        for right in range(len(cards)):
            store[cards[right]] += 1
            while store[cards[right]] == 2:
                ans = min(ans, right - left + 1)
                store[cards[left]] -= 1
                left += 1
        return ans if ans != float('inf') else -1