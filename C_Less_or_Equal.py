n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
if k == 0:
    if nums[0] == 1:
        print(-1)
    else:
        print(1)
else:
    if k < len(nums):
        if nums[k - 1] == nums[k]:
            print(-1)
        else:
            print(nums[k - 1])
    else:
        print(nums[k - 1])
