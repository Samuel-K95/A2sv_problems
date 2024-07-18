# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

n = int(input())
nums = list(map(int, input().split()))
 
nums.sort()
dup = [0] * n
i = 0
for j in range(0, len(nums), 2):
    dup[j] = nums[i]
    i += 1
for j in range(1, len(nums), 2):
    dup[j] = nums[i]
    i += 1
 
flag = True
for j in range(1, len(nums), 2):
    if dup[j] < dup[j - 1]:
        flag = False
        break
for i in range(2, len(nums), 2):
    if dup[i] > dup[i-1]:
        flag = False
        break
if flag:
    print(*dup)
else:
    print("Impossible")