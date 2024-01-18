class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        check = len(t)
        count = 0
        t_count = Counter(t)
        store = defaultdict(int)
        ans = float('inf')
        fin_lef = 0
        fin_righ = 0
        for right in range(len(s)):
            store[s[right]] += 1
            if store[s[right]] <= t_count[s[right]]:
                count += 1
            while left < len(s) and  count == check:
                if right - left + 1 < ans:
                    fin_lef = left
                    fin_righ = right
                    ans = right - left + 1
                if s[left] in t_count and store[s[left]] == t_count[s[left]]:
                    count -= 1                    
                store[s[left]] -= 1
                left += 1
        return s[fin_lef:fin_righ+1] if ans != float('inf') else ""                