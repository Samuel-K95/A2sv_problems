# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

t = int(input())
def solve():
    n = int(input())
    s = 9 if n > 9 else n
    ans = []
    while n > 0:
        ans.append(str(s))
        n -= s
        if n > 9:
            s -= 1
        else:
            s = min(s-1, n)

    ans.reverse()
    print(int("".join(ans)))



for _ in range(t):
    solve()