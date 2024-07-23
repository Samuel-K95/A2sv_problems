# Problem: B - Tzuyu and Sana - https://codeforces.com/gym/532814/problem/B

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a^b)