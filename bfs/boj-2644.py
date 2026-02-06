# BOJ 1644 - 촌수계산
import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
visited[a] = 0
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)
q = deque([a])
while(q):
    x = q.popleft()
    for i in family[x]:
        if visited[i] == -1:
            visited[i] = visited[x]+1
            if i == b:
                print(visited[i])
                sys.exit()
            q.append(i)
        
print(visited[b])

## 시간 복잡도 : O(n + m) => 탐색할 때 각 정점과 간선을 한 번씩만 방문하기 때문(그래프생성은 O(n)이라 포함)
## 배운 점: 
# - sys.exit()으로 프로그램 아예종료하는 방법도 있음
# - 조기종료 가능한지 한 번 더 고민해보기