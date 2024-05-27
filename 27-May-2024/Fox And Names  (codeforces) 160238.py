# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque


n = int(input())
stack = []
graph = defaultdict(list)
vis = set()
indeg = defaultdict(int)
ans = True
for _ in range(n):
    s = input()
    if stack:
        diff = True
        top = stack[-1]
        fir, sec = 0, 0
        while fir < len(top) and sec < len(s):
            if top[fir] != s[sec]:
                diff = False
                graph[top[fir]].append(s[sec])
                indeg[top[fir]] += 0
                indeg[s[sec]] += 1
                break
            fir += 1
            sec += 1
        if diff and len(top) > len(s):
            ans = False
    stack.append(s)
queue = deque()
for i in indeg:
    if indeg[i] == 0:
        queue.append(i)
        vis.add(i)

alphabet = []
while queue:
    front = queue.popleft()
    alphabet.append(front)
    for neigh in graph[front]:
        indeg[neigh] -= 1
        if indeg[neigh] == 0 and neigh not in vis:
            queue.append(neigh)
            vis.add(neigh)

for i in range(26):
    curr = chr(i + 97)
    if curr in indeg:
        continue
    alphabet.append(curr)


if len(alphabet) < 26 or not ans:
    print("Impossible")
else:
    print("".join(alphabet))


