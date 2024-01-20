class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left = 0
        store = defaultdict(int)
        for right in range(len(fruits)):
            store[fruits[right]] += 1
            while len(store) > 2:
                store[fruits[left]] -= 1
                if store[fruits[left]]  == 0:
                    del store[fruits[left]] 
                left += 1
            ans = max(ans, right - left + 1)   
        return ans 