# Problem: A - Balanced Subsequence - https://codeforces.com/gym/532814/problem/A

from collections import Counter


n, k = map(int, input().split())

s = input()

track = Counter(s)

small = float('inf')
is_all = set()
for i in track:
    if ord(i) - 65 <= k:
        small = min(small, track[i])
        is_all.add(i)

if len(is_all) == k:
    print(small * k)
else:
    print(0)

