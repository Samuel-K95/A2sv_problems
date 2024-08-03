# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    if n >= 3:
        if n % 3 == 0:
            ans = n // 3
        else:
            rem = (n // 3) * 3
            n_rem = n - rem
            if n_rem < 2:
                ans = (n // 3) + 1
            else:
                ans = (n // 3) + 1
    else:
        if n == 1:
            ans = 2
        elif n == 2:
            ans = 1
            
    print(ans)
    
