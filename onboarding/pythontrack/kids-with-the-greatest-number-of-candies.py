class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        dup = [ i for i in candies]
        dup.sort()
        trg = dup[-1]
        ans = []
        for i in candies:
            if i + extraCandies >= trg:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        

        