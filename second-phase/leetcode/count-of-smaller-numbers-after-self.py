class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            first, second= 0, 0
            add = 0
            ret = []
            while first < len(arr1) and second < len(arr2):
                if arr2[second][0] < arr1[first][0]:
                    add += 1
                    ret.append([arr2[second][0], arr2[second][1], arr2[second][2]])
                    second += 1
                else:
                    ret.append([arr1[first][0], arr1[first][1], arr1[first][2] + add])
                    first += 1
            
            while first < len(arr1):
                ret.append([arr1[first][0], arr1[first][1], arr1[first][2] + add])
                first += 1
            
            if second < len(arr2):
                ret.extend(arr2[second:])
            
            return ret

        def mergesort(left, right):
            if left == right:
                return [[nums[left], left, 0]]
            mid = left + (right - left) // 2

            left = mergesort(left, mid)
            right = mergesort(mid+1, right)

            return merge(left, right)
        

        computed = mergesort(0, len(nums) - 1)
        ans = [0] * len(nums)

        for i in computed:
            ans[i[1]] = i[2] 

        return ans
