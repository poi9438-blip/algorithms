# BOJ 1707 - 이분 그래프
import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(n):
    q = deque([n])
    visited[n] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            elif visited[x] == visited[i]:
                return False
    return True

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    answer = True
    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    for i in range(1,V+1):
        if visited[i]==0:
            answer = bfs(i)
            if not answer: break
    if answer: print('YES')
    else: print('NO')
            

## 시간 복잡도 :  O(V + E) => 각 정점과 간선을 적어도 한 번 이상 방문해야하기에 
## 배운 점: 문제에 대해 이해가 안되면 꼭 먼저 분석하고 넘어가기