# BOJ 3184 - 양
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
visited = [list(sys.stdin.readline().strip()) for _ in range(R)]
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
sheeps = 0 
wolfs = 0


def bfs(si, sj):
    wolf = 0
    sheep = 0
    q = deque([(si, sj)])
    if visited[si][sj]=='v': wolf+=1
    elif visited[si][sj]=='o': sheep+=1
    visited[si][sj] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<R and 0<=nj<C and (visited[ni][nj] != '#' and visited[ni][nj] !='0') :
                if visited[ni][nj]=='v': wolf+=1
                elif visited[ni][nj]=='o': sheep+=1
                visited[ni][nj] = '0'
                q.append((ni, nj))
    if wolf<sheep: return (sheep, 0)
    else: return (0, wolf)

for i in range(R):
    for j in range(C):
        if visited[i][j] != '#' and visited[i][j] !='0':
            sheep, wolf = bfs(i, j)
            sheeps += sheep
            wolfs += wolf
print(sheeps, wolfs)
        

## 시간 복잡도 : O(R × C) => 한번씩 다 들러서 확인해야하기 때문에
## 배운 점: 없음 ㅎㅎ 