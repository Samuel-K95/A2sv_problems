# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

from collections import defaultdict


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    pref = [0 for _ in range(52)]
    for _ in range(n):
        l, r = map(int, input().split())
        if l <= k <= r:
            pref[l] += 1
            pref[r + 1] += -1
    
    mx = 0
    count = defaultdict(int)
    for i in range(1, 52):
        pref[i] += pref[i-1]
        if pref[i] >= pref[mx]:
            mx = i
        count[pref[i]] += 1
    
    # print(count, mx)
    if mx == k and count[pref[mx]] == 1:
        print("YES")
    else:
        print("NO")
