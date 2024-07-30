# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n = int(input())
s = input()
ans = []
p, t = 0, 1
while p < n:
    ans.append(s[p])
    p += t
    t += 1
print("".join(ans))