# BOJ 7562 - 나이트의 이동
import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [-2, -1, -2, -1, 1, 2, 1, 2]
dy = [1, 2, -1, -2, 2, 1, -2, -1]
for _ in range(T):
    l = int(sys.stdin.readline())
    startX, startY = map(int, sys.stdin.readline().split())
    endX, endY = map(int, sys.stdin.readline().split())
    
    visited = [[-1 for _ in range(l)] for _ in range(l)]
    visited[startX][startY] = 0

    q = deque([(startX, startY)])
    while q:
        x, y = q.popleft()
        if x==endX and y==endY: 
            print(visited[x][y])
            break # 시간초과 해결
        for i in range(8):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<l and 0<=yy<l and visited[xx][yy] == -1:
                visited[xx][yy] = visited[x][y]+1
                q.append((xx, yy))
            
    

## 시간 복잡도 : O(T × l²) => 모든 칸을 한번씩 봐야해서
## 배운 점: 조기종료