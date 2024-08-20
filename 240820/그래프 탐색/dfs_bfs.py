# 단위 기능을 잘 구현해보자
import sys
from collections import deque

input = sys.stdin.readline
N,M,V = tuple(map(int,input().split()))
board = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = tuple(map(int,input().split()))
    board[a].append(b)
    board[b].append(a)
for i in range(1,N+1):
    board[i].sort()

def dfs(v):
    ans_dfs.append(v)
    visited[v] = True
    for n in board[v]:
        if not visited[n]:
            dfs(n)

def bfs(s):
    q = deque()
    q.append(s)
    ans_bfs.append(s)
    visited[s] = True
    while q:
        c = q.popleft()
        for n in board[c]:
            if not visited[n]:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = True

ans_dfs = []
ans_bfs = []
visited = [False] * (N+1)
dfs(V)
visited =[False] * (N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
