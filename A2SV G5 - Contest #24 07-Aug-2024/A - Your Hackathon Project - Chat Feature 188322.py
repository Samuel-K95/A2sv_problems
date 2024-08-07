# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] != ')':
            break
        cnt += 1
    rem = n - cnt
    if cnt > rem:
        print("Yes")
    else:
        print("No")
