# Problem: C - Removal Hack - https://codeforces.com/gym/534160/problem/C

from collections import defaultdict
from heapq import heappop, heappush


import sys

def input():
    return sys.stdin.readline()

def main():
    n = int(input())
    child = defaultdict(int)
    not_child = defaultdict(int)

    not_par = []
    parent = defaultdict(int)
    children = defaultdict(list)

    for i in range(1, n + 1):
        p, r = map(int, input().split())
        parent[i] = p
        child[p] += 1
        children[p].append(i)

        if r == 1:
            not_child[p] += 1
            heappush(not_par, i)

    ans = []
    while not_par:
        front = heappop(not_par)
        if child[front] == not_child[front]:
            ans.append(front)
            p = parent[front]

            child[p] += child[front]
            not_child[p] += not_child[front]

    if ans:
        print(*ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()





