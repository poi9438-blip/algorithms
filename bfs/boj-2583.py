# BOJ 2583 - 영역 구하기
import sys
from collections import deque

BLOCKED, UNVISITED, VISITED = -1, 0, 1

M, N, K = map(int, sys.stdin.readline().split())
visited = [[UNVISITED]*N for _ in range(M)]
areas = []
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]


for _ in range(K):
    startX, startY, endX, endY  = map(int, sys.stdin.readline().split())
    for j in range(startY, endY):
        for i in range(startX, endX):
            visited[j][i] = BLOCKED

def bfs(si, sj):
    area = 1
    q = deque([(si, sj)])
    visited[si][sj] = VISITED
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<M and 0<=nj<N and visited[ni][nj] == UNVISITED:
                visited[ni][nj] = VISITED
                area+=1
                q.append((ni, nj))
    return area
for i in range(M):
    for j in range(N):
        if visited[i][j]==UNVISITED:
            areas.append(bfs(i,j))
areas.sort()
print(len(areas))
print(*areas)
        
        

## 시간 복잡도 : O(M × N) => 모든 격자를 한번씩 (정렬하는수가 상대적으로 적기에 정렬은 무시 가능)
## 배운 점: x와 y가 반대로 들어와서 헷갈린 문제 => 입력받을때만 유의하자!