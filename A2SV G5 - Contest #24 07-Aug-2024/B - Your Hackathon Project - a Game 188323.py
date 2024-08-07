# Problem: B - Your Hackathon Project - a Game - https://codeforces.com/gym/534160/problem/B

n , m = map(int, input().split())

a = list(map(int, input().split()))

pref = [0]
for i in range(1, n):
    diff = 0
    if a[i] - a[i-1] < 0:
        diff = abs(a[i] - a[i-1])
    pref.append(pref[-1] + diff)

suff = [0]

for i in range(n-2, -1, -1):
    diff = a[i] - a[i+1]

    if diff < 0:
        suff.append(suff[-1] + abs(diff))
    else:
        suff.append(suff[-1])

for _ in range(m):
    s, t = map(int, input().split())

    if t > s:
        print(pref[t-1] - pref[s-1])
    else:
        st = n - s
        en = n - t
        print(suff[en] - suff[st])