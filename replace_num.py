x = int(input())
for i in range(x):
    y = int(input())
    nums = list(map(int, input().split()))
    max_ = nums[0]
    ans = 0
    for j in range(1, y):
        store = sum(nums[1:j])
        if store == max_:
            if ans < (j - 1):
                ans = j - 1
    print(ans)
