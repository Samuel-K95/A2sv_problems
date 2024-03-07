class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == '|']

        ans = []
        for left, right in queries:
            start = bisect_left(candles, left)
            end = bisect_right(candles, right)
            number_of_candles = end - start 
            length = 0
            if candles and start < len(candles) and end > 0 and end-1 <len(candles):
                length = candles[end-1] - candles[start] + 1
            plates = length - number_of_candles
            if plates > 0:
                ans.append(plates)
            else:
                ans.append(0)
        return ans
