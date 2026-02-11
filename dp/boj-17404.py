# BOJ 17404 - RGB거리 2
import sys
n = int(sys.stdin.readline())
INF = 10**9

RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = INF

for k in range(3):
    prev = [INF]*3
    prev[k] = RGB[0][k]
    for i in range(1,n):
        cur = [INF]*3
        for j in range(3):
            cur[j] = min(prev[j-1], prev[j-2]) + RGB[i][j]
        prev = cur
    ans = min(ans, prev[k-1], prev[k-2])

print(ans)

## 시간 복잡도 : O(n) (입력 배열 제외하면 O(1))
## 배운 점: dp는 이전에 뭘 선택했는지 기억하지 못한다, 기억하게 하려면 추가로 처리하는 부분이 필요