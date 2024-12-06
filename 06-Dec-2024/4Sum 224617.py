# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        vis = set()
        nums.sort()
        for ol in range(len(nums)):
            for o_r in range(len(nums)-1, ol, -1):
                l, r = nums[ol], nums[o_r]
                il, ir = ol+1, o_r-1
                curr = l + r
                while il < ir:
                    iln, irn = nums[il], nums[ir]
                    if curr + (iln + irn) > target:
                        ir -= 1
                    elif curr + (iln + irn) < target:
                        il += 1
                    else:
                        if (l, iln, irn, r) not in vis:
                            ans.append([l, iln, irn, r])
                            vis.add((l, iln, irn, r))
                        il += 1
                        ir -= 1
        return ans

