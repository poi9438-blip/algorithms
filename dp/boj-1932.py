# BOJ 1932 - 정수 삼각형
import sys
n = int(sys.stdin.readline())
dp = []

for i in range(n):
    tree = list(map(int, sys.stdin.readline().split()))
    new_dp = [0]*(i+1)
    if i==0:
        new_dp = [tree[0]]
    else:
        for j in range(len(tree)-1):
            new_dp[j] = max(new_dp[j], dp[j]+tree[j])
            new_dp[j+1] = max(new_dp[j+1], dp[j]+tree[j+1])
    dp = new_dp

print(max(dp))

## 시간 복잡도 : O(n²) (공간복잡도 O(n))
## 배운 점: 배열을 꼭 만들어야만 하는 상황인지 체크하기