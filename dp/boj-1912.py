# BOJ 1912 - 연속합
import sys
n = int(sys.stdin.readline())
dp = list(map(int, sys.stdin.readline().split()))

cur = dp[0]
ans = dp[0]

for i in range(1, n):
    cur = max(dp[i], cur+dp[i])
    ans = max(ans, cur)
print(ans)

## 시간 복잡도 : O(n) (입력배열 제외하면 공간복잡도 O(1))
## 배운 점: 시간/공간복잡도를 줄인다고 다 좋은 코드는 아님(가독성, 원본배열 유지 등 고려해야 함)