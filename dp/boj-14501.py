# BOJ 14501 - 퇴사
import sys
N = int(sys.stdin.readline())
dp = [0]*(N+1)
for i in range(0,N):
    T, P = map(int, sys.stdin.readline().split())
    dp[i+1] = max(dp[i+1], dp[i])
    if i+T<=N:
        dp[i+T] = max(dp[i+T], dp[i]+P)

print(dp[N])

## 시간 복잡도 : O(N) (공간복잡도도 O(N))
## 배운 점: 
# - 기준을 문제 조건에서 찾지 말고 데이터의 패턴에 집중하기
# - 배열을 꼭 만들어야만 하는 상황인지 체크하기