for _ in range(int(input())):
    x = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    set_ = list(set(nums))
    num = len(set_) - 1
    i = 0
    re = 0
    while i < num:
        if set_[i + 1] - set_[i] <= 1:
            re += 1

        i += 1
    if len(set_) - re == 1:
        print("YES")
    else:
        print("NO")
