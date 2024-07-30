# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

from collections import defaultdict, deque
import sys


def input():
    return sys.stdin.readline().strip()

def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for potions in p:
        c[potions-1] = 0

    p = set(p)
    
    graph = defaultdict(list)
    indeg = [0] * n

    for idx in range(n):
        m = list(map(int, input().split()))

        if idx + 1 not in p:
            indeg[idx] += m[0]
            for k in range(1, len(m)):
                graph[m[k]-1].append(idx)

    ans = [0] * n

    queue = deque()
    vis = set()

    for i in range(n):
        if indeg[i] == 0:
            queue.append(i)
            ans[i] = c[i]
            vis.add(i)
    
    while queue:
        front = queue.popleft()
        ans[front] = min(ans[front], c[front])

        for neigh in graph[front]:
            if neigh + 1 not in p:
                ans[neigh] += ans[front] 

            indeg[neigh] -= 1

            if indeg[neigh] == 0 and neigh not in vis:
                queue.append(neigh)
                vis.add(neigh)

    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

