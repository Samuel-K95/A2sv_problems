class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        ans = float('inf')
        store = defaultdict(int)
        for right in range(len(blocks)):
            store[blocks[right]] += 1
            if right - left + 1 == k:
                ans = min(ans, store['W'])
                store[blocks[left]] -= 1
                left += 1
        return ans