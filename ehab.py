x = int(input())
nums = list(map(int, input().split()))
even, odd = 0, 0
for i in range(x):
    if nums[i] % 2 == 0:
        even += 1
    else:
        odd += 1
if even == 0 or odd == 0:
    for i in nums:
        print(i, end=" ")
else:
    nums.sort()
    for i in nums:
        print(i, end=" ")
