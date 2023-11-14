n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
ans = []
for i in range(m):
    try:
        while a[x] < b[i]:
            x += 1
    except:
        pass
    ans.append(x)
for i in ans:
    print(i, end=" ")
