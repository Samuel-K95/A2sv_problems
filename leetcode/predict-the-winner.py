class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def recur(left, right, turn):
            if left > right:
                return 0
            
            res = 0
            if turn == 1:
                l = nums[left] +  recur(left + 1, right, 2)
                r = nums[right] + recur(left, right - 1, 2)
                return max(l, r)
            else:
                l = recur(left + 1, right, 1)
                r =  recur(left, right - 1, 1)
                return min(l, r)

        
        ans = recur(0, len(nums)-1, 1)

        return (sum(nums) - ans) <= ans
